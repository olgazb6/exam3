class Tomato:

    states = {1:'weed', 2:'bush', 3:'flower', 4:'tomato'}     #стадии созревания томата

    def __init__(self, index):
        self._index = index
        self._states = 1

    def grow(self):                         # переводит томат на следующую стадию созревания
        if self._states < 4:
            self._states += 1
        self._print_state()
        # print(self._states)

    def is_ripe(self):                      # проверка, что томат созрел
        if self._states == 4:
            return True
        else:
            return False

    def _print_state(self):                        # выводит на какой стадии томаты
        print(f'Tomato {self._index} is {Tomato.states[self._states]}')

class TomatoBush:

    def __init__(self, count):                                              # count - количество томатов
        self.tomatoes = [Tomato(index) for index in range(1, count+1)]      #создать список объектов класса Tomato

    def grow_all(self):                         # переводит все объекты из списка томатов на следующий этап
        for i in self.tomatoes:
            i.grow()

    def all_are_ripe(self):                     # проверка, что все томаты созрели
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):                      # чистит список томатов после сбора урожая
        self.tomatoes = []
        print('-------------')
        print('Урожай собран!')

class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):                       # садовник работает, томат переходит на след стадию роста
        print('-------------')
        print('Садовник работает')
        self._plant.grow_all()

    def harvest(self):                        # проверяет, все ли плоды созрели.
        if self._plant.all_are_ripe():        # Если все -садовник собирает урожай.
            print('Все плоды созрели')
            self._plant.give_away_all()
        else:                                 # Если нет - метод печатает предупреждение
            print('Не все плоды созрели!')

    def knowledge_base(self):                  # справка
        print(f'Справка: садовник {self.name} выращивает томаты.')



tomato = TomatoBush(5)
gardener = Gardener('Tom', tomato)

gardener.knowledge_base()

gardener.work()
gardener.harvest()
gardener.work()
gardener.work()
gardener.harvest()



