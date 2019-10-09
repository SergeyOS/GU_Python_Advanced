from argparse import ArgumentParser
from common.JIM_config import *
from common.JIM_protocol import *


# Анализ параметров коммандной строки
def parse_args_console(argv):
    """
    Обработка параметров командой строки
    :param argv: параметры командной строки или None
    :return: адрес и порт сервера
    """
    if argv is None:
        return DEFAULT_LISTEN_ADDRESS, DEFAULT_LISTEN_PORT

    parser = ArgumentParser()
    parser.add_argument(
        '-a', '--address', type=str, default=DEFAULT_LISTEN_ADDRESS,
    )
    parser.add_argument(
        '-p', '--port', type=int, default=DEFAULT_LISTEN_PORT,
    )
    args = parser.parse_args(argv)
    if args.port < 1024 or args.port > 65535:
        raise ValueError
    return args.address, args.port


def validate_message(msg: str):
    """
    Проверка запроса на обязательные поля
    :param msg: текст сообщения
    :return: факт соответствия запроса формату
    """
    if JIM_ACTION in msg and JIM_TIME in msg:
        return True
    return False
