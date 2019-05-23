# This file contains objects that aggregate other objects #
from Objects import *
import pygame


class Container:  # Parent class for all objects that aggregate other objects
    def __init__(self):
        self.list = []

    def add(self, obj):
        self.list.append(obj)

    def draw(self):
        for item in self.list:
            item.draw()
    
    def get_list(self):
        return self.list


class Player(Container):  # Stores pieces
    def __init__(self):
        super().__init__()
        self.selection = ''  # Stores the selected piece

    def check_mouse_pos(self, mouse_pos, mouse_pressed, enemy):
        for item in self.list:
            if item.getX() <= mouse_pos[0] <= item.getX() + item.getWidth() and item.getY() <= mouse_pos[1] <= item.getY() + item.getHeight():
                if mouse_pressed[0] == 1:
                    item.posMovement(self.list, enemy.getList())

