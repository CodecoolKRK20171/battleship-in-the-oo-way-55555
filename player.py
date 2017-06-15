from ocean import Ocean
from ship import Ship
from square import Square


class Player:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
