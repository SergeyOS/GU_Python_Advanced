#  4. Преобразовать слова 'разработка', 'администрирование', 'protocol', 'standard' из строкового представления 
#  в байтовое и выполнить обратное преобразование (используя методы encode и decode).


str_list = ['разработка', 'администрирование', 'protocol', 'standard']
for spam in str_list:
    encode_word = spam.encode('utf-8')
    print(f'Байтовое представление слова "{spam}" (encode): {encode_word}')
    decode_word = encode_word.decode('utf-8')
    print(f'Строковое представление слова "{encode_word}" (decode): {decode_word}')
