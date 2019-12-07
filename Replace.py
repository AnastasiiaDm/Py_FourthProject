print('\n11. Дана строка. Замените в этой строке все появления буквы `h` на букву `H`, кроме первого и последнего вхождения.\n')

s = 'yyyyhhhhh yyyyyhhhhh  yyyyyyyyhhhh yyyyyyy'
h = "h"
start = s.find(h)
# print('start = ', start, s[start])
afterStart = start + 1
# print('afterStart = ', afterStart)
end = (s.rfind(h))
# print('end = ', end)
afterend = end + 1
# print('afterend = ', afterend)

print(s[:start:], s[start], s[afterStart:end].replace('h', 'H'), s[end], s[afterend:], sep='' )

