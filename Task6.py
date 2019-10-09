#  6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет»,
#  «декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.


str_list = ['сетевое программирование', 'сокет', 'декоратор']
file_name = "test_file.txt"

with open(file_name, "w") as f_n:
    lines = map(lambda x: x + '\n', str_list)
    f_n.writelines(lines)
default_encoding = 'utf-8'
with open(file_name, "r") as f_n:
    default_encoding = f_n.encoding
    print(f'Кодировка файла {file_name}: {default_encoding}')

with open(file_name, "r", encoding='utf-8', errors='replace') as f_n:
    for spam in f_n:
        print(spam)

with open(file_name, "rb") as f_n:
    for spam in f_n:
        eggs = spam.decode(default_encoding).encode('utf-8')
        print(eggs.decode('utf-8'))
