# 1

# a = (1,2,3,4,5,6)          #Кортеж
# b = (1,)                 #Кортеж
# print(a,b)

# 2

# a = (1, 2, 3, 4, 5, 6)
# b = [1, 2, 3, 4, 5, 6]
# print(a.__sizeof__())              # Определяет размер занимаемой памяти
# print(b.__sizeof__())
# print(a[::3])                      # Срезы работают так же как и в списках
# print(a[2::2])

# 3

# a = (1, 2, 3, 'abc', 54)
# print(a)
# # a[0]= 12         # кортеж неизменянемый тип данных
# b = tuple()        # функция кортеж
# c = list()         # функция список
# print(b)
# print(c)

# 4

# a = (1, 2, 3, 'abc', 54)
# a = list(a)
# print(a)
# a.append(75)
# print(a)
# a = tuple(a)
# print(a)

# 5

# a = (1, 2, 3, ['abc', 1, 2], 54)
# a[3].append(45)
# print(a)
# print(a[0]+10)

# 6
# a = (1, 2, 3, 'abc', 54)
# print(len(a))
# b = (8, 7, 54)
# z = a + b
# print(z)
# v = a * 2 # Применяется так же как и к спискам
# print(v)
# print(v.count(1))


# 7

# a = (34, 6, 15, 100, 200)
# print(max(a))        # К спискам тоже приминяются
# print(min(a))       # К спискам тоже приминяются
# print(sum(a))       # К спискам тоже приминяются

# 8

# a = ('asd', 'sd', 'asddas')

# print(max(a, key=len))  # к спискам тоже применяется
# print(min(a, key=len))  # к спискам тоже применяется
# for i in a:
#     print(i, len(i))
# ind_max = a.index(max(a, key=len))
# print(a[ind_max], len(a[ind_max]))

# 9

# import random
#
# c = [random.randint(0,100) for i in range(10)]
# c = tuple(c)
# print(c)
# print(max(c))
# print(min(c))

# 10

import random

# c = [random.randint(0,10) for i in range(10)]
# d = [random.randint(-5,0) for i in range(10)]
# e = tuple(c) + tuple(d)
# print(e, e.count(0))

# 11

a = ('sd', 'weriq', 'ggg', 1, 88)
# e = ','.join(a)
print(', '.join([str(i) for i in a]))

# 12
# A = (13, 5, 43, 49, 67, 32, 12, 98, 6, 10, 34, 20, 55, 68, 14, 60, 14)
# B = (53, 21, 4, 23, 76, 3, 43, 12, 54, 342, 21)
# a = sum(A)
# b = sum(B)
# if a > b:
#     print('Сумма в кортеже больше - А =', a)
# else:
#     print('Сумма в кортеже больше - В =', b)
# print('Порядковый номер списка А', A.index(min(A)) + 1)
# print('Порядковый номер списка В', B.index(min(B)) + 1)
