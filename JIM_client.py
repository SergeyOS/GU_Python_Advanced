from common import JIM_utils
from common.JIM_protocol import *
from common.JIM_config import *
import sys
import socket
import json
from datetime import datetime


class ClientJim:
    # класс описывающий работу клиента
    __transport_socket: socket.socket = socket.socket()
    __server_address = DEFAULT_LISTEN_ADDRESS
    __server_port = DEFAULT_LISTEN_PORT
    __login = 'Guest'
    __password = ''
    __connection_status = False

    def __init__(self, login: str, password: str, argv=None):
        """
        Инициализация клиента
        :param login: логин пользователя
        :param password: пароль пользователя
        :param argv: параметры командной строки, содержашие порт и адрес сервера
        """
        self.__server_address, self.__server_port = JIM_utils.parse_args_console(argv)
        self.__login = login
        self.__password = password

    def __connect(self):
        """
        Инициализация подключения к серверу
        """
        try:
            self.__transport_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__transport_socket.connect((self.__server_address, self.__server_port))
            self.__connection_status = True
        except ConnectionRefusedError:
            print('Не удалось подключиться к серверу')
            self.__connection_status = False
        return self.__connection_status

    def __write(self, msg: str):
        """
        Отправка сообщения через сокет
        :param msg: сообщение в формате протокола
        """
        if self.__connection_status:
            self.__transport_socket.send(msg.encode(DEFAULT_ENCODING))

    def __read(self) -> str:
        """
        Чтение данных из сокета
        :return:сообщение
        """
        if self.__connection_status:
            response_msg = self.__transport_socket.recv(BUFFER_SIZE)
            return response_msg.decode(DEFAULT_ENCODING)
        else:
            return ''

    def __send_request_to_server(self, dict_msg: dict):
        """
        Отправка сообщения серверу и получение ответа
        :param dict_msg: справочник сообщения с полями сообещния
        """
        request_msg = json.dumps(dict_msg)
        if JIM_utils.validate_message(request_msg):
            if self.__connect():
                self.__write(request_msg)
                response_msg = self.__read()
                self.__process_response(response_msg)
        else:
            print('Не верный формат сообщения')

    def __process_response(self, msg: str):
        """
        Обработка ответа сервера
        :param msg: тект ответа
        """
        response_msg = json.loads(msg)
        print(response_msg)

    # Функции формирующие сообщения

    def send_presence(self):
        """
        Формирование и отправка на сервер presence-сообщение
        """
        msg_text = {JIM_ACTION: JIM_PRESENCE,
                    JIM_TIME: datetime.now().timestamp(),
                    JIM_TYPE: 'status',
                    JIM_USER: {JIM_LOGIN: self.__login,
                               JIM_PASSWORD: self.__password
                               }
                    }
        self.__send_request_to_server(msg_text)


if __name__ == "__main__":
    client = ClientJim('Guest', '', sys.argv[1:])  # hack отсекаем текущий файл
    client.send_presence()
