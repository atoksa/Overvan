# import random
# a = random.randint(1, 10)
# b = random.randint(1, 2)
# print(a)
# print(b)
# if b == 1:
#     b = 'red'
#     print(b)
# else:
#     b = 'black'
#     print(b)
#
# i = 0
# while i < 5:
#     c = int(input('Введите число: '))
#     d = input('Введите цвет: ')
#     if a == c and b == d:
#         print('Вы угадали')
#         break
#
#     else:
#         print('Повторите попытку')
#         i += 1

# От Оксаны

# import random
#
# nam, color = random.randint(1, 10), random.randint(1, 2)
# # print(nam, color)
# if color == 1:
#     color = 'красное'
# elif color == 2:
#     color = 'черное'
# victory = (str(nam) + ' ' + color)
# print(victory)
#
# tr = 0      # счетчик попыток
# tr_2 = 5    # обратный отсчет попыток
# while tr <= 5:
#     player = input('Введите число от 0 до 10 и цвет (красное или черное): ')
#     tr += 1
#     tr_2 -= 1
#     if player == victory:
#         print('Вы угадали!')
#         print('☺️ '*30)
#         break
#     elif tr_2 == 0:
#         print('Вы не угадали. \n Попыток больше не осталось.\nПравильная комбинация: ' + victory)
#         break
#     else:
#         print('Вы не угадали, попробуйте еще раз.\n Осталось попыток:' + ' ' + str(tr_2))
#         print('-'*30)