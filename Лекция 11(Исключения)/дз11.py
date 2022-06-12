# Ввод с клавиатуры. Если строка введённая с клавиатуры – это числа, то поделить первое на второе.
# Обработать ошибку деления на ноль. Если второе число 0, то программа запрашивает ввод чисел заново.
# Также если были введены буквы, то обработать исключение.
i = 0
while i == 0:
    q = input('Введите первое число: ')
    w = input('Введите второе число: ')
    if q.isalpha() or w.isalpha():
        try:
            wer = float(q) / float(w)
        except ValueError:
            print('Введены буквы')
    elif q.isdigit() and w.isdigit():
        try:
            wer = float(q) / float(w)
        except ZeroDivisionError:
            print('Деление на ноль')
        else:
            print(wer)
            break


