# 1
# d = {}
# d = {'Ключ' : 1, 'Ключ2' : 2}               # сначала пишется ключ, а потом значение
# print(d)
# 2

# d = dict(short ='dict', long='dictory')
# d_2 = dict([(1,1),(2,4)])           # Словарь кортежей!!!
# print(d, '\n', d_2)

# 3

# d = dict.fromkeys(['a','b'])
# d_2 = dict.fromkeys(['a','b'], 100)            # Присваевымаем каждому ключ значение 100
# print(d, '\n', d_2)

# 4

import random

a = ['a', 'b', 'c']
d = {i:random.randint(1,10) for i in a}
print(d)

d_2 = [3,9,4]
print(d_2[0])

print(d['a'])                    # Обращение к словарю через ключ

d['v'] = 33                       # Добавление в словарь
print(d)
d['a'] = 100                      # Меняем значение ключа
print(d)
print(len(d))                        # Длина словаря


# 5

# d = {1:3, 'a':23, 5 : 311, 6 : 'ff'}
# del d['a']                              # Удаляем значение из словаря по ключу
# print(d)

# 6
#
# d = {'phone' : ['iphone', 'nokia', 'samsung'],
#      'car' : ['kia', 'bmw', 'tesla'],
#      'dict1' : {'a': 123, 'b':'Hello'}
#     }
# print(d)
# print(d['car'][1])
# print(d['dict1']['b'])
# print(len(d))
# if 'car' in d:
#     print('CAR!')


# 7
#
# # Операция not in - определение отсутствия ключа в словаре
# # Формирование словаря слов с их числовым эквивалентом
#
# # 1. Сформировать пустой словарь
# Words = dict()  # Words = {}
#
# # 2. Ввести количество слов в словаре
# count = int(input("Количество слов в словаре: "))
#
# # 3. Цикл добавления слов
# i = 0
# while i < count:
#     print("Ввод слов")
#     wrd = input("Слово:")
#     value = int(input("Значение: "))
#
#     # Если ключа wrd нет в словаре, то добавить пару [wrd:value]
#     if wrd not in Words:
#         Words[wrd] = value
#     i = i + 1
# # Вывести сформированный словарь
# print(Words)

# 8

# N = dict(zip([1,2,3],['One','Two','Three']))        # Создание словаря из двух списков ключей и значений при помощи функции zip
# print(N)

# 9

# d = {'phone' : ['iphone', 'nokia', 'samsung'],
#      'car' : ['kia', 'bmw', 'tesla'],
#      'dict1' : {'a': 123, 'b':'Hello'}
#     }
# for key in d:
#         print(key)
#         print(key, '-', d[key])
# print(d.items())
# for key,values in d.items():         # функция создания кортежей
#     print(key, '--', values)

# 10 Создайте словарь person, в котором будут присутствовать ключи name, age, city.
# Выведите значение возраста из словаря person.

# person = {'name': 'Anton', 'age': 28, 'city': 'Mogilev'}
# print(person['age'])

# 11 Значениями словаря могут быть и списки.
# Создайте словарь с ключами BMW, Tesla и списками из 3х моделей в качестве значений.
# Выведите первое и последнее значения каждого из ключей.

# d = {'BMW': ['M3', 'X7', 'E31'], 'Tesla': ['Модель 3', 'Модель Х', 'Модель S']}
# print(d['BMW'][0], d['Tesla'][0])
# print(d['BMW'][-1], d['Tesla'][-1])

# 12 Дан словарь с числовыми значениями. Необходимо их все перемножить и вывести на экран.
# import random
#
# a = ['a', 'b', 'c']
# d = {i: random.randint(1, 10) for i in a}
# print(d)
# r = 1
# s = 0
# for key, values in d.items():
#     print(values)
#     r *= values
#     s += values
# print(r)
# print(s)