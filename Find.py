# s = "Пользователь вводит, отдельно, строку `s` и один символ `ch`. Необходимо выполнить поиск в строке `s` всех символов `ch`."
s = 'вf b`ch` ch.'
ch = 'ch'
symb = 0

print('s = ' ,s)


print('sting = ', s.find(ch))

for search in s:
    i = search.find(ch)
    print('i = ', i)
    if i == ch:
        symb += 1
print(s[symb], i)





# result = searchCH.find(ch)
# print("result = ", ch, result)







    # if ch in s:
    #     print(i, ch)
    #     i += 1

# s.find(ch)
# for ch in s:
#     print(ch)

    # if ch :
    #     print(s.find(ch), symbol)
# for ch in s:
#     print(s.find(ch))

# i = 1
# for color in 'red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'violet':
#     print('#', i, ' color of rainbow is ', color, sep='')
#     i += 1

