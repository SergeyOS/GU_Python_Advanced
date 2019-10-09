#  3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.


spam = b'attribute'
print(f'"attribute" без ошибок возможно записать в байтовом виде: {spam}')

# spam = b'класс'
print(
    f'"класс" преобразовать невозможно в байтовый тип. Ошибка: SyntaxError: bytes can only contain ASCII literal characters. ')

# spam = b'функция'
print(
    f'"функция" преобразовать невозможно в байтовый тип. Ошибка: SyntaxError: bytes can only contain ASCII literal characters. ')

spam = b'type'
print(f'"type" без ошибок возможно записать в байтовом виде: {spam}')
