from math import sqrt
import random


class SeaMap:
    def __init__(self, size_map: int):
        self.map = [i+1 for i in range(size_map*size_map)]
        self.map_ship = self.map.copy()
        self.ship1 = int(size_map * 0.4)
        self.ship2 = int(size_map * 0.3)
        self.ship3 = int(size_map * 0.2)
        self.ship4 = int(size_map * 0.1)


    def shoot(self):
        # !добавляет ка карту результат выстрела
        pass

    def cell(self):
        pass

    def print_map(self):
        # !вывод поля боя в консоль
        for i in range(int(sqrt(len(self.map)))):
            for j in range(int(sqrt(len(self.map)))):
                print(self.map[j + i*int(sqrt(len(self.map)))], end="\t")
            print("\n")

    def shot(self, number):
        if number in self.map_ship:
            a = self.map_ship.index(number)
            if isinstance(self.map[a], int):
                self.map[a] = "."
            else:
                self.map[a] = "[X]"

        else:
            print("Сюда уже выстел был...")

    def ships(self):
        for i in range(3):
            self.r1 = random.randint(1, len(self.map) + 1)
            self.r2 = random.choice([self.r1-1, self.r1+1, self.r1-10, self.r1+10])
            self.a = self.map.index(self.r1)
            self.b = self.map.index(self.r2)
            self.map[self.a] = "[]"
            self.map[self.b] = "[]"


sm = SeaMap(10)
sm.ships()

sm.print_map()
s = int(input("> "))
sm.shot(s)
sm.print_map()
