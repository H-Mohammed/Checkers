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
    
    def getList(self):
        return self.list
    
    def CheckMousePos(self,MousePos,MousePressed,enemy):
        for item in self.list:
            if item.getX() <= MousePos[0] <=  item.getX()+item.getWidth() and item.getY() <= MousePos[1] <= item.getY()+item.getHeight():
                if MousePressed[0] == 1:
                    item.posMovement(self.list,enemy.getList())

                


class Player(Container):  # Stores pieces
    def __init__(self):
        super().__init__()

