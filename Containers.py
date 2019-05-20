# This file contains objects that aggregate other objects #
from Objects import *


class Container:  # Parent class for all objects that aggregate other objects
    def __init__(self):
        self.list = []

    def add(self, obj):
        self.list.append(obj)

    def draw(self):
        for item in self.list:
            item.draw()



class Player(Container):  # Stores pieces
    def __init__(self):
        super().__init__()

