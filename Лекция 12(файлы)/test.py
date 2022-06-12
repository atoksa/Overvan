# 1

# f = open('1.txt', 'r')
# print(f)
# print(*f)

# 2

# f = open('1.txt', 'r', encoding='utf-8') # Кодировка поддерживает русские буквы
# print(f)
# print(*f)
# f.close()

# 3

# f = open('1.txt', 'r', encoding='utf-8')
# try:
#     print(*f)  # работа с файлом
# finally:
#     f.close()

# 4

# with open('1.txt', 'r', encoding='utf-8') as f:
#     s = f.read()
#
#
# print(s, type(s))

# 5

# with open('1.txt', 'r', encoding='utf-8') as f:
#     # print(f.readline())       # Читает 1 строку
#     # print(f.readline())       # Читает 2 строку
#     # print(f.readlines())      # Читает 3 строку
#     s = f.readlines()
# print(s)
# s_new = []
# for i in s:
#     i = i.replace('\n', '')
#     print(i)
#     s_new.append(i)
# print(s_new)

# 6

# with open('2.txt', 'w') as f:
#     f.write('Hello \nWorld')

import os

# os.rename('2.txt', 'test.txt')                # Переменовать
# print('Текущая директория', os.getcwd())      # Где находиться
# os.mkdir('folder')                            # Создание папки
# os.chdir('folder')                              # Переход в папку
# print('Текущая директория', os.getcwd())
# with open('1.txt', 'w') as f:                  # Создали в папке folder файл 1
#     f.write('Hello \nWorld')
# print('Текущая директория', os.getcwd())



# print('Текущая директория', os.getcwd())
# os.chdir('folder')                                    # Переход в папку folder
# print('Текущая директория', os.getcwd())
# os.chdir('..')                                        # Переход в нижнию папку
# print('Текущая директория', os.getcwd())
#
# os.makedirs('n1/n2/n3')                           # Создание дерево папок



# os.remove('folder/1.txt')       # Удаления файла с папки
# os.rmdir('folder')              # Удаления обязательно пустой папки



# os.removedirs('n1/n2/n3')               # Создание дерево папок


# В файле, в одну строку записаны слова и числа через пробел или _ найти сумму всех чисел.

# with open('task_1.txt') as f:
#     s = f.read()
#     print(s)
#
# s = s.replace('_', ' ')
# a = s.split()
# print(a)
# s = 0
# for i in a:
#     if i.isdigit():
#         i = int(i)
#         s += i
# print(s)

#Файл содержит числа и буквы. Каждый записан в отдельной строке.
# Нужно считать содержимое в список так,
# чтобы сначала шли числа по возрастанию, а потом слова по возрастанию их длинны.


# with open('task_2.txt') as f:
#     s = f.readlines()
# print(s)
# b = []
# n = []
# for i in s:
#     i = i.replace('\n', '')
#     if i.isalpha():
#         b.append(i)
#     elif i.isdigit():
#         n.append(int(i))
# print(b, n)
# n.sort()
# b.sort(key=len)
# mas = n + b
# print(mas)



