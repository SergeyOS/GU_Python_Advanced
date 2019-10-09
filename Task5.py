#  5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com
#  и преобразовать результаты из байтовового в строковый тип на кириллице.

import subprocess
import chardet

list_sites = ['yandex.ru', 'youtube.com']
for site in list_sites:
    args = ['ping', site]
    subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    print(f'Answer {site}:')
    for line in subproc_ping.stdout:
        line_encoding = chardet.detect(line)['encoding']
        line = line.decode(line_encoding).encode('utf-8')
        print(line.decode('utf-8'))
