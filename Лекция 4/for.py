#1
# for i in range(4):
#     print(i)
#     print('Привет')

#2


# for i in range(1,10,2):
#     print(i)

# a = 10
# b = 0
# c = -2
# for i in range(a,b,c):
#     print(i, end='     ')

#3

# a = 'Я учу Python'
# for i in a:
#      print(i)
#     if i == 'P':
#         print('Python')

#4

#Необходимо ввести числа от 1 до 15 в порядке убывания
# for i in range(15,0,-1):
#     print(i, end=' ')

#5

# a = 'я учу PYTHON python'
# b = ''
# for i in a:
#     # print(i)
#     if i.isupper():
#         print(b)
#         b = b + i
# print('Результат', b )

#6

# a = input('Введите строку: ')
# b = input('Введите символ: ')
# c = ''
# for i in a:
#     # print(i)
#     if i != b:
#         # print(c)
#         c = c + i
# print(c)

#7

# a = int(input('Введите начало: '))
# b = int(input('Введите конец: '))
# c = int(input('Введите шаг: '))
#
# for i in range(a, b, c):
#     print(i, end=' ')

#8

# a = [1 , 45, 7, 8, 9, 0] # массив чисел
# a_s = ['hello', 'world', 'abc'] # массив строк
# print(a, len(a))
# print(a_s, len(a_s))
# for i in a:
#     print(i)
#     if i == 7:
#         break              # Останавливает цикл
# print('Готово')
#
# for i in a:
#     if i == 7:
#         continue
#     print(i)
# print('Готово')

#9

# a = [1, 2, 12, 2, 2, 4, 3, 6, 7]
# b = []
# for i in a:
#     if i % 2 == 0:
#         b.append(i)
# print(b)
# b.append(123)
# print(b)
# print('Цифра повторяется 2: ', a.count(2))


# a = [1, 2, 12, 2, 2, 4, 3, 6, 7]
# c = 0
#
# for i in a:
#     # print(c)
#     c = c + i
# print('Результат', c)




