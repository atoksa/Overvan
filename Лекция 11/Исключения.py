# 1

# try:
#     a = 100/0
# except ZeroDivisionError:
#     a = 0
# print(a)

# 2

# try:
#     int('dfs')
# except Exception as e:                  # Действует на все виды исключений
#     print('Произошла ошибка', e)

# 3

# a = {'a' : 1, 'b': 2}
# try:
#     value = a['c']                        # Для множества
# except KeyError:
#     print('Ключа не существует')
#
# b = [1,2,3,4]
# try:
#     b[5]                                    # Для списка
# except IndexError:
#     print('Нет такого индекса')

# 4

# a = {'a' : 1, 'b': 2}
# try:
#     b = a['c']
# except IndexError:
#     print('Нет такого индекса')
# except KeyError:
#     print('Нет ключа в словаре')
# except:
#     print('Произолша другая ошибка')
# finally:
#     print('Оператор finnally выполнен')               # Выполняется всегда

# 5

# a = {'a' : 1, 'b': 2}
# try:
#     b = a['c']
# except (IndexError, KeyError):
#     print('Ошибка IndexError или KeyError')
# else:
#     print('Ошибок не произошло')                    #  Выполниться если ошибок нет
# finally:
#     print('Оператор finnally выполнен')


# 6
# Введите два числа с клавиатуры.
# Поделите одно на другое. Обработайте ошибку деления на ноль, если ошибок нет, то результат деления возвести в квадрат.
# Также используйте оператор finally.

# a = int(input('Введите число: '))
# b = int(input('Введите число: '))
# try:
#     c = a/b
# except ZeroDivisionError:
#     c = 0
#     print('Делить на ноль нельзя')
# else:
#     d = c**2
#     print(d)
# finally:
#     print('Оператор finnally выполнен')

