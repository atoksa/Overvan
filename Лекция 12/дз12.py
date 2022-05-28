with open('дз12.txt', 'w', encoding='utf-8') as f:
    i = 1
    while i != 0:
        q = input('Введите данные: ')
        if q == '':
            break
        else:
            f.write(q)
            f.write('\n')
f = open('дз12.txt', 'r', encoding='utf-8')
s = f.readlines()
s_new = []
for i in s:
    i = i.replace('\n', '')
    # print(i)
    s_new.append(i)
print(s_new)

