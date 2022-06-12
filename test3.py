# # 1. Напишите функцию, которая будет принимать номер кредитной карты и
# # показывать только последние 4 цифры. Остальные цифры должны заменяться
# # звездочками
#
# a = input('Введите номер карты: ')
# def karta():
#    return  a[8:12]
# print('**** **** ****',karta())

# 2. Напишите функцию, которая проверяет: является ли слово палиндромом
# a = 'qadddaq'
# def palidrom():
#     if a[:] == a[::-1]:
#         print('Палидром')
# palidrom()

# 3

class Tomato:
    states = {1 : 'flower', 2 : 'green', 3 : 'red'}

    def __init__(self,index,state,states):
        self._index = index
        self._state = states[1]
    def grow(self,states):
        if self._state == 'flower':
            self._state = states[2]
        elif self._state == 'green':
            self._state = states[3]
    def is_ripe(self,states):
        if self._state == states[3]:
            return 'Томат созрел'

class TomatoBush:
    def __init__(self,num):
        self.tomatoes = [Tomato(i) for i in range(num)]
    def grow_all(self, states):
        if self._state == 'flower':
            self._state = states[2]
            return self._state, self.tomatoes
        elif self._state == 'green':
            self._state = states[3]
            return self._state, self.tomatoes
    def all_are_ripe(self):
        if self._state == 'red':
            return 'True'
    def give_away_all(self):
        if self._state == 'red':
            self.tomatoes = []


class Gardener:
    def __init__(self,name,plant):
        self.name = name
        self.__plant = plant
    def work(self,states):
        if self._state == 'flower':
            self._state = states[2]
            return 'Садовник работает', self._state
        elif self._state == 'green':
            self._state = states[3]
            return 'Садовник работает', self._state
    def harvest(self):
        if self._state == 'red':
            return 'Садовник собирает урожай'
        else:
            return "Урожай не созрел"
    @staticmethod
    def knowledge_base():

        return self.states, self.tomatoes

print(Gardener.knowledge_base())

