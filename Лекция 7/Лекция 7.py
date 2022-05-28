#1

# print("100 200 300 400".count("0"))
# print("100 200 300 400".count("0", 3, 7))
# print("100 200 300 400".count("0", 3))

# 2

# a = 'asdyuwqeinqk '
# g = 0
# s = 0
# gl = 'aeuyio'
#
# for i in a:
#     if i in gl:
#         g += 1
#         print(i)
#     else:
#         s += 1
# print('Гласные: ', g)
# print('Согласные: ', s)
# print('Согласные: ', len(a) - g)

# 3

# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# c = int(input('Введите третье число: '))
#
# if a > b and a < c:
#     print('Среднее число:', a)
# elif b > a and b < c:
#     print('Среднее число:', b)
# else:
#     print('Среднее число:', c)
#
#
# d = [a, b, c]
# d.sort()
# print('Среднее число: ', d[1])

# 4
# Список из 7 цифр. Если четных цифр в нем больше чем нечетных, то найти сумму всех его цифр, если нечетных больше,
# то найти произведение 1 3 и 6 элемента.


# s = [1, 2, 3, 4, 5, 6, 7]
# ch = 0
# nech = 0
# for i in s:
#     if i % 2 == 0:
#         ch += 1
#     else:
#         nech += 1
# print('Чётные: ', ch, 'Нечётные: ', nech)
# if ch > nech:
#     sm = sum(s)                                  # Определяет сумму списка
#     print('Сумма: ', sm)
# elif nech > ch:
#     pr = s[0] * s[2] * s[5]
#     print('Произведение: ', pr)

# 5

# a = int(input('Введите число: '))
# b = str(a)
# print(b[::-1])


#  6


# import random
#
# c = [random.randint(1, 10) for i in range(10)]
# print(c)
#
# d = sum(c)
# print(d)
#
# a = 1
# for i in c:
#     a *= i
# print(a)

# 7
#Вводиться строка. Удалить из неё все пробелы. После этого определить, является ли она палиндромом(перевертышем),
#т.е. одинаково пишется, как сначала, так и с конца

# s = input('Введите строку: ')
# n_s = s.replace(' ', '')
# print(n_s)
# if n_s == n_s[::-1]:
#     print('Cрока палиндром')
# else:
#     print('Не палиндром')