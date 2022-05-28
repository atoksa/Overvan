a = float(input('Введите число: '))
b = input('Введите действие: ')
с = float(input('Введите число: '))

if b == '-':
    print('Ответ: ', a - с)
elif b == '+':
    print('Ответ: ', a + с)
elif b == '/':
    print('Ответ: ', a / с)
elif b == '*':
    print('Ответ: ', a * с)
elif b == '+':
    print('Ответ: ', a + с)
elif b == '**':
    print('Ответ: ', a ** с)
elif b == '//':
    print('Ответ: ', a // с)
elif b == '%':
    print('Ответ: ', a % с)
else:
    print('Ошибка')
