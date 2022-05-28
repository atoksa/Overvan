# 1

# e = [1, 2, 'f', 6, 'b']
# print(e)
# e = list()
# e = []

# 2

# import random
#
# c = [random.randint(0,9) for i in range(10)]
#
# print(c)
# print(c[0], c[-1])
# print(c[2:])
#
# c.append(777)
# c.append('Hi')
# print(c)

# 3

# l = [123, 544, 'fsdfsd', 3213, 3]
# l.insert(0,'Hello')                           # Не заменяет,а пододвигает
# l.insert(3,777)
# print(l)
# l[3] = 'world'                                # Замена в списке
# print(l)

# 4

# l = [123  , 544, 'fsdfsd', 3213, 3, 555, 'BBB']
# del l[2]                                       # Функция удалить
# print(l)
#
# l.remove(3213)                                  # Функция удалить
# print(l)

# 5 Проверка есть ли в списке

# l = [123, 544, 'fsdfsd', 3213, 3, 555, 'BBB']
# print(123 in l)
#
# if 123 in l:
#     print('Yes')

# 6

# a = [1, 2, 3, 'as']
# b = [4, 5, 6]
# print(a + b)
# c = a + b
# print(c)
#
# d = ['a', 'b', 'c']
# d.extend(c)                                   # Дополняем список d
# print(d)

# 7

# a = [1, 2, 3, 'as']
# b = a                                       # Ссылка на список по этому одинаковые id и добовляется в один и тот же список
# b.append(77)
# a.append(66)
# print(id(a), id(b))
# print(a, b)
# c = a.copy()                                # Копируем и будут разыне id, добовляет в список который скопировали
# c.append('asd')
# print(id(a), id(c))                         # Проверяем id

# 8 Одно и тоже только через разные циклы

# a = [1, 2, 3, 4]
# for i in a:
#     print(i)
#
# print('-'*20)
#
# b = [1, 2, 3, 4]
# b_l = len(b)
# i = 0
# while i < b_l:
#     print(b[i])
#     i += 1

# 9

# a = [1, 2, 3, 4]
# a.clear()                               # Очищает список
# print(a)
# b = [1, 2, 3, 4, 1, 1, 3, 1]
# print(b.count(1), 'Индекс элемена 4: ',  b.index(4))
# x = b.pop(4)                            # Удаляет ,но сохраняет в переменную
# print(b)
# print(x)
# b.reverse()                             # Переворачивает список
# print(b)

# 10

# b = [1, 6, 3, 4, 2, 5, 3, 1]
# b.sort()                        # Сортировка
# print(b)
# b.sort(reverse=True)            # Обратная сортировка
# print(b)
#
# s = ['asd', 'sdf', 'a']
# s.sort(key=len)                 # Сортировка по длине
# print(s)
# s.sort()                        # Сортировка по Unicode
# print(s)

# 11

# a = [1, 6, 3, 4, 'q', [3,6,7]]
# print(a[5][2])              # Выводим из  списка в списке


# 12 Дан произвольный список.Предстаивть его в обратом порядке в двух видах

# b = [1, 6, 3, 4, 2, 5, 3, 1]
# b.reverse()
# print(b)
#
# c = [1, 6, 3, 4, 2, 5, 3, 1]
# print(c[::-1])

# 13

# b = [1, 2, 5, 9, 3, 4, 20, 1]
# a = b.index(20)
# print(a)
# b[a] = 200
# print(b)


