from SeaMap import *


class Ship(SeaMap):
    def random_ship(self):
        print(self.map)

    def user_ship(self):
        pass


s = Ship(5)
s.random_ship()