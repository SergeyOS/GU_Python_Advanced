from socket import socket
from common import JIM_utils
from common.JIM_config import *
from common.JIM_protocol import *
import sys
import socket
import json


class ServerJim:
    # класс описывающий работу сервера
    __transport_socket: socket.socket = socket.socket()

    def __init__(self, argv=None):
        """
        Инициализирует сокет сервера
        :param argv: параметры командной строки с информацией о порте и адресе
        """
        try:
            listen_address, listen_port = JIM_utils.parse_args_console(argv)
            # Подготовка сокета
            self.__transport_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__transport_socket.bind((listen_address, listen_port))
        except ValueError:
            print('Порт задан неверно')

    # Запуск сервера
    def start(self):
        """
        Запускает сервер. Прослушивает сокет. Получает сообщения и формирует ответ
        """
        if self.__transport_socket is not None:
            self.__transport_socket.listen(MAX_CONNECTIONS)
            try:
                while True:
                    client_socket, client_address = self.__transport_socket.accept()
                    data = client_socket.recv(BUFFER_SIZE)
                    message_from_client = data.decode(DEFAULT_ENCODING)
                    self.__log(f'Получено: {message_from_client}')
                    self.__process_request(client_socket, message_from_client)
                    client_socket.close()
            finally:
                if self.__transport_socket is not None:
                    self.__transport_socket.close()
        else:
            print('Не удалось инициализировать сокет')

    def send_response(self, client: socket, msg: dict):
        """
        Отправляет ответ на запрос
        :param msg: справочник содержащий код и текст ответа
        :type client: object сокет клиента

        """
        response_msg = json.dumps(msg)
        self.__log(f'Отправлено: {response_msg}')
        client.send(response_msg.encode(DEFAULT_ENCODING))

    def msg_response(self, code: int, text: str) -> dict:
        """
        Формирует сообщение ответа
        :param code: код сообщения
        :param text: текст сообщения
        :return: справочник
        """
        msg = {JIM_RESPONSE: code}
        if code > 300:
            msg['error'] = text
        else:
            msg['alert'] = text
        return msg

    def __process_request(self, client:socket, msg:str):
        """
        Обработка запросов
        :param client: сокет клиента, приславшего запрос
        :param msg: строка, содержащая запрос согласно протоколу
        """
        if JIM_utils.validate_message(msg):
            json_request = json.loads(msg)
            if json_request[JIM_ACTION] == JIM_PRESENCE:
                self.send_response(client, self.msg_response(JIM_CODE_OK, 'Добро пожаловать'))
        else:
            self.send_response(client, self.msg_response(JIM_CODE_MSG_NOT_VALID, 'Нет обязательных полей'))

    def __log(self, text:str):
        """
        Логирует сообешения. На текущий момент в консоль
        :param text: текст сообщения
        """
        print(text)


if __name__ == "__main__":
    server = ServerJim(sys.argv[1:])  # hack отсекаем текущий файл
    server.start()
