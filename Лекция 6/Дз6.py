a = [4, 6, 'ру', 'tell', 78]
b = [44, 'hello', 56, 'exept', 3]
c = a + b
print(c)
c.insert(3, 6)
print(c)
d = []
for i in c:
   if type(i) != str:
       d.append(i)
print(d)
print(len(c))



