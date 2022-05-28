# b = 1
# for i in range(1, 100):
#     if i % 2 != 0:
#         b = b + i
# print('Результат:', b)



# a = []
# for i in range (1,500):
#     if i % 5 == 0:
#         a.append(i)
# print(a)


# for i in range(1,497):
#     if i % 2 == 0:
#         print(i)


a = [1, 2, 3, 3, 4, 6, 7, 3, 4, 3]
b = []

for i in a:
    if a.count(i) >= 2 and i not in b:
        print(i)
        b.append(i)
print(b)


