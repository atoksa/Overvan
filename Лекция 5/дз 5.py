
while True:
    a = float(input('Введите число: '))
    b = float(input('Введите число: '))
    c = input('Введите операцию: ')
    if c == '+':
        print('Ответ: ',a + b)
    if c == '-':
        print('Ответ: ', a - b)
    if c == '*':
        print('Ответ: ', a * b)
    if c == '**':
        print('Ответ: ', a**b)
    elif b == '//':
        print('Ответ: ', a // b)
    elif b == '%':
        print('Ответ: ', a % b)
    elif c == '/' and b == 0:
        print('Делить на 0 нельзя')
        break