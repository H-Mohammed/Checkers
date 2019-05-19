# This file contains objects that aggregate other objects #
from Objects import *


class Container:  # Parent class for all objects that aggregate other objects
    def __init__(self):
        self.list = []

    def draw(self):
        for item in self.list:
            item.draw()


class Board(Container):  # Used to make the checker board
    def __init__(self, surface):
        super().__init__()
        self.surface = surface

        for y in range(8):
            for x in range(8):
                if (x + y) % 2 == 0:
                    self.list.append(Square(self.surface, (0, 0, 0), (x*60, y*60), (60, 60)))
                else:
                    self.list.append(Square(self.surface, (255, 255, 255), (x * 60, y * 60), (60, 60)))