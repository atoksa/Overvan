# a = 'Преобразовать, текст, в, кортеж, слов, с, удалением, знаков, препинания'
# r = tuple(str(i) for i in a.split(','))
#
# e = str(r)
# print(r)
# b = ''
# for i in e:
#     if i != ',':
#         b+=i
# print(b)
# c = max(r, key=len)
# print(c,len(c))



import os
t = '''Many - desktop__publishingiiii packages~ and web? [page] editors\ now use Lorem Ipsum as their default model text,
and a_search for! 'lorem ipsum' will^ uncover {many} web... sites still in their
infancy.'''
print('\033[95;5;1mТескт:\033[0m ', t, '\n', '~' * 50)
a = '''.-'!?()[]{}@#$%/"*:;<>\,~&^'''   # строка со знаками препинания, кроме нижнего подчеркивния
c = ''
for i in t:                             # циклом делаем замену нижнего подчеркивания на пробел, т.к. предполагается что он разделяет 2 слова
    if i == '_':                        # но если он просто внутри слова, то его надо было добавить в строку "а"
        c += i                          # а если оно и между слов и внутри слова - как тогда быть?
        t = t.replace(i, ' ')
    elif i in a:                        # и добавляем пропущенные знаки в новую переменную
        c += i
t = ''.join(i for i in t if i not in a)     # заменяем все знаки препинания из "а" на пустое значение
print('\033[95;5;1mКортеж из слов:\033[0m ', tuple(t.split()), '\n', '~' * 50)      # преобразуем строку t в список, а потом в кортеж
print('\033[94;5;1mСамое длинное слово в кортеже:\033[0m ', max(tuple(t.split()), key=len), '\n',
      '~' * 50)  # по ключу len находим самое длинное слово в кортеже
print('\033[92;3;5mКоличество букв самого длинного слова:\033[0m ', len(max(tuple(t.split()), key=len)), '\n', '~' * 50)
print('\033[91;5;1mПропущенные символы:\033[0m ', c)
print('\033[93;5;6m☻\033[0m')