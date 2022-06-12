# a = [1, 2, 3, 4, 5]
# a[2:3] = []
# print(a)

# a = (1,2,3)               # Верно
# b = [1,2,3]
# c = tuple('fdsf')             # Верно
# e = tuple(b)                  # Верно
# r = tuple(tuple(b))               # Верно


# a = '1дана 1строка'
# b = ''
# for i in a[::-1]:
#     b += i
# print(b)
# e = b.replace('1','one')
# print(e)
# или
# s = input()
#
# first_word = s[:s.find(' ')]
# second_word = s[s.find(' ') + 1:]
# k = second_word + ' ' + first_word
# print(k)
# print(k.replace('1', 'one'))


# for i in range(1, 10):
#     print(i, i * 2, i * 3, i * 4, i * 5, i * 6, i * 7, i * 8, i * 9)
# или
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i * j,end="  " )
#     print(" ")

# Сгенерировать список из 10 чисел. Диапазон чисел - 0, 9.
# Посчитайте, сколько в нем пар элементов, равных друг другу.
# Любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. При этом образованная пара не участвуют в формировании других пар.
# Вывести цифру из списка '-' количество пар с этой цифрой.
# Например, [1, 1, 1, 1].
# 1 - 2
# Результат: 2 пары.

# import random
#
# a = [random.randint(0, 9) for i in range(10)]
# print(a)
# p = 0
# for i in set(a):
#     p += a.count(i) // 2
#     print(i, '-', a.count(i) // 2)
# print('Всего пар:', p)

# Даны два кортежа:
# A = (13, 5, 43, 49, 67, 32)
# B = (53, 21, 4, 23)
# Необходимо определить:
# 1) Сумма элементов какого из кортежей больше и вывести соответствующее сообщение на экран ( Сумма больше в кортеже - ..)
# 2) Вывести на экран порядковые номера минимальных элементов этих
# кортежей

# a = (13, 5, 43, 49, 67, 32)
# b = (53, 21, 4, 23)
# if sum(a)> sum(b):
#     print('Сумма чисел больше в A')
# else:
#     print('Сумма чисел больше в B')
# print(a.index(min(a))+1)
# print(b.index(min(b))+1)

# a = [1, 2, 3]
# b = ['qwe', 'asd', 'zxc']
# print(dict(zip(a, b)))

# a = [1, 2, 3, 4, 5, 6]
# b = [3, 8, 5, 1, 0, 7]
# print(set(a) & set(b),'\n', 'Количество повторений:',len(set(a) & set(b)))



# with open('21.txt', 'r', encoding='utf-8') as f:
#     print('Количество строк: ', len(f.readlines()))
#
# with open('21.txt', 'r', encoding='utf-8') as f:
#     s = f.readlines()
# for i in s:
#     i = i.replace('\n', '')
#     print(i, len(i))
