# 1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку
# определенных данных из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый
# «отчетный» файл в формате CSV. Для этого:
# a. Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с
# данными, их открытие и считывание данных. В этой функции из считанных данных
# необходимо с помощью регулярных выражений извлечь значения параметров
# «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения
# каждого параметра поместить в соответствующий список. Должно получиться четыре
# списка — например, os_prod_list, os_name_list, os_code_list, os_type_list. В этой же
# функции создать главный список для хранения данных отчета — например, main_data
# — и поместить в него названия столбцов отчета в виде списка: «Изготовитель
# системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих
# столбцов также оформить в виде списка и поместить в файл main_data (также для
# каждого файла);
# b. Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой
# функции реализовать получение данных через вызов функции get_data(), а также
# сохранение подготовленных данных в соответствующий CSV-файл;
# c. Проверить работу программы через вызов функции write_to_csv().

import csv
import os
import re

DATA_PATH = 'data'


# инициализируем список файлов
def init_path_to_datafiles():
    input_files = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    return map(lambda x: os.sep.join([DATA_PATH, x]), input_files)


# готовит 1 строку для каждого из четырех списков
# возвращает номер добавленной строки
def init_row(list_four_lists):
    for i in range(len(list_four_lists)):
        list_four_lists[i].append(None)
    return len(list_four_lists[0]) - 1


# получает из файлов list_files данные и записывает в список
def get_data(list_files):
    params = [
        'Изготовитель системы',
        'Название ОС',
        'Код продукта',
        'Тип системы'
    ]
    main_data = [params]
    os_list = [[], [], [], []]  # инициалиазция четырех списков  os_prod_list, os_name_list, os_code_list, os_type_list
    # 4 списка - требование условий задачи
    for file_name in list_files:
        current_row = init_row(os_list)
        # на 1 файл - 1 строка с данными
        with open(file_name, "r") as f_n:
            for line in f_n:
                for i in range(len(params)):
                    if re.match(params[i], line):
                        os_list[i][current_row] = line.split(':')[-1].strip()

    for i in range(len(os_list[0])):
        main_data.append([os_list[0][i], os_list[1][i],
                          os_list[2][i], os_list[3][i]
                          ])
    return main_data


def write_to_csv(result_file_name):
    main_data = get_data(init_path_to_datafiles())
    with open(result_file_name, 'w', newline='') as f_n:
        f_n_writer = csv.writer(f_n, quoting=csv.QUOTE_NONNUMERIC, delimiter='\t')
        f_n_writer.writerows(main_data)


# Проверка записанного файла
def test_result(path_result_file):
    with open(path_result_file) as f_n:
        print(f_n.read())


path_result_file = os.sep.join([DATA_PATH, 'result_task1.csv'])
write_to_csv(path_result_file)
test_result(path_result_file)