# После переписи населения есть список фамилий. Вывести фамилии и их количество повторений.
# Сколько всего разных фамилий.

# a = ['Акимов', 'Анисимов', 'Акимов', 'Азарин', 'Абрамчук', 'Азарин', 'Анисимов', 'Анисимов', 'Акимов', 'Акимов',
#      'Величко', 'Бабко', 'Величко', 'Кучко', 'Петрова']
#
# print('Всего фамилий:', len(set(a)))
# for i in a:
#     print(i, a.count(i))

# Спортлото 6 из 36
# Игрок имеет билет с номерами от 1 до 36, он выбирает на нем (вводит в ручную), какие 6 номеров, по его предположению, выпадут.
# За 2 совпавших номера выигрыш составляет 50р., 3 совпавших - 150р., 4 совпавших - 1 000р.,
# 5 совпавших - 10 000р., 6 совпавших - 300 000р.
# После проведения розыгрыша выводятся выпавшие номера, выводится билет с отмеченными номерами, выводятся совпавшие номера, их количество и выигрыш.
# билет на печать не нужно выводить

# import random
# a = {random.randint(1, 36) for i in range(6)}
# print(a)
# i = 0
# c = []
# while i < 6:
#     b = int(input('Введите шесть номеров от 1 до 36: '))
#     c.append(b)
#     i += 1
# if len(set(a) & set(c)) == 2:
#     print('Вы выйграли 50р')
# elif len(set(a) & set(c)) == 3:
#     print('Вы выйграли 150р')
# elif len(set(a) & set(c)) == 4:
#     print('Вы выйграли 1000р')
# elif len(set(a) & set(c)) == 5:
#     print('Вы выйграли 10000р')
# elif len(set(a) & set(c)) == 6:
#     print('Вы выйграли 300000р')



