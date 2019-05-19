# This file contains classes that make individual objects #
import pygame


class Objects:  # This is the parent class used to make any objects
    def __init__(self, surface, color, pos):
        self.color = color
        self.pos = pos
        self.surface = surface
        self.x = pos[0]
        self.y = pos[1]


class Checker(Objects):  # This is used to make the checker pieces
    def __init__(self, surface, color, pos):
        super().__init__(surface, color, pos)
        self.radius1 = 30  # Radius of larger circle
        self.radius2 = 25
        pygame.draw.circle(self.surface, self.color, self.pos, self.radius1)
        pygame.draw.circle(self.surface, (150, 0, 0), self.pos, self.radius2)

    def draw(self):
        pygame.draw.circle(self.surface, self.color, self.pos, self.radius1)
        pygame.draw.circle(self.surface, (150, 0, 0), self.pos, self.radius2)


class Square(Objects):  # This is used to make the board
    def __init__(self, surface, color, pos, size):
        super().__init__(surface, color, pos)
        self.size = size
        self.height = size[1]
        self.width = size[0]
        self.rect = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.surface, self.color, self.rect)

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)
