# 3. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий
# сохранение данных в файле YAML-формата. Для этого:
# a. Подготовить данные для записи в виде словаря, в котором первому ключу
# соответствует список, второму — целое число, третьему — вложенный словарь, где
# значение каждого ключа — это целое число с юникод-символом, отсутствующим в
# кодировке ASCII (например, €);
# b. Реализовать сохранение данных в файл формата YAML — например, в файл
# file.yaml. При этом обеспечить стилизацию файла с помощью параметра
# default_flow_style, а также установить возможность работы с юникодом:
# allow_unicode = True;
# c. Реализовать считывание данных из созданного файла и проверить, совпадают ли они
# с исходными.

import yaml
import random
import os

DATA_PATH = 'data'
YAML_FILE = 'result_task3.yaml'


def generate_text():
    spam_dict = {}
    spam_dict['first_key'] = [random.randint(1, 100) for i in range(1, 5)]
    spam_dict['second_key'] = random.randint(200, 1000)
    spam_dict['third_key'] = {x: ''.join([str(y + random.randint(10, 100)), ' ₽']) for x, y in zip(range(4), range(4))}
    return spam_dict


def write_yaml(yaml_file_path):
    yaml_file_path = os.sep.join([DATA_PATH, YAML_FILE])

    with open(yaml_file_path, 'w', encoding='utf-8') as f_n:
        yaml.dump(generate_text(), f_n, default_flow_style=False, allow_unicode=True)


# Проверка записи
def test_result(yaml_file_path):
    with open(yaml_file_path, 'r', encoding='utf-8') as f_n:
        print(f_n.read())


yaml_file_path = os.sep.join([DATA_PATH, YAML_FILE])
write_yaml(yaml_file_path)
test_result(yaml_file_path)
