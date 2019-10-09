# 2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
# (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.


str_list = [b'class', b'function', b'method']
for spam in str_list:
    print(f'Type: {type(spam)}, value: {spam}, length: {len(spam)}')
