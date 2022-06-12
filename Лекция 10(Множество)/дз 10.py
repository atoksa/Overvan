# Дано три случайных списка, необходимо найти в этих списках одинаковые числа и определить чья сумма чисел больше четных или нечетных
import random
a = [random.randint(1, 100) for i in range(100)]        # Создал три случйаных списка
b = [random.randint(1, 100) for i in range(100)]
c = [random.randint(1, 100) for i in range(100)]
d = set(a) & set(b) & set(c)                             # Нашел совпадения
print(d)
y = 0
r = 0
for i in d:
    if i % 2 == 0:                                       # Разделил на четных и нечетных
        y += i
    else:
        r += i
print(y)
print(r)
if y > r:
    print('Сумма четных больше')                         #  Нашел чья сумма больше
else:
    print('Сумма нечетных больше')





