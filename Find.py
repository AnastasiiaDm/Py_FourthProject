s = "chch c h Пользователь вводит, отдельно, строку `s` и один символ `ch`. Необходимо выполнить поиск в строке `s` всех символов `ch`."
ch = 'ch'
symb = -1
cnt = 0

print('s = ', s, '\nSymbols IDs: ')

while True:
    symb = s.find(ch, symb+1)
    if symb < 0:
        break
    cnt +=1
    print(symb, symb+1, sep=', ')
print('Count of \'ch\' symbol:', cnt)