# 2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с
# информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными. Для
# этого:
# a. Создать функцию write_order_to_json(), в которую передается 5 параметров — товар
# (item), количество (quantity), цена (price), покупатель (buyer), дата (date). Функция
# должна предусматривать запись данных в виде словаря в файл orders.json. При
# записи данных указать величину отступа в 4 пробельных символа;
# b. Проверить работу программы через вызов функции write_order_to_json() с передачей
# в нее значений каждого параметра.


import json
import os
import datetime
import random

DATA_PATH = 'data'
JSON_FILE = 'orders.json'


def write_order_to_json(item, quantity, price, buyer, date):
    data = {'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date
            }

    json_file_path = os.sep.join([DATA_PATH, JSON_FILE])

    with open(json_file_path) as f_n:
        json_obj = json.load(f_n)
    json_obj['orders'].append(data)

    with open(json_file_path, 'w', encoding='utf-8') as f_n:
        json.dump(json_obj, f_n, indent=4)


def generate_item():
    items = ['one', 'two', 'three', 'four', 'five']
    item = random.choice(items)
    quantity = round(random.uniform(1, 35), 2)
    price = round(random.uniform(10, 5000), 2)
    buyers = ['OLIVER', 'JACK', 'HARRY', 'JACOB', 'CHARLIE']
    buyer = random.choice(buyers)
    start = datetime.date(2019, 1, 1)
    end = start + datetime.timedelta(days=365)
    random_date = start + (end - start) * random.random()
    return item, quantity, price, buyer, random_date.strftime('%d-%m-%Y')


# Проверка записи
def test_result():
    json_file_path = os.sep.join([DATA_PATH, JSON_FILE])

    with open(json_file_path, encoding='utf-8') as f_n:
        json_text = f_n.read()
        print(json_text)


write_order_to_json(*generate_item())
test_result()
