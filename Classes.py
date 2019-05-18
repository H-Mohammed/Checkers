# This file contains classes for running the game #
import pygame


class Objects:  # This is the parent class used to make any objects
    def __init__(self, surface, color, pos):
        self.color = color
        self.pos = pos
        self.surface = surface
        self.x = pos[0]
        self.y = pos[1]


class Checker(Objects):
    def __init__(self, surface, color, pos):
        super().__init__(surface, color, pos)
        self.radius1 = 30  # Radius of larger circle
        self.radius2 = 25
        pygame.draw.circle(self.surface, self.color, self.pos, self.radius1)
        pygame.draw.circle(self.surface, (150, 0, 0), self.pos, self.radius2)

    def draw(self):
        pygame.draw.circle(self.surface, self.color, self.pos, self.radius1)
        pygame.draw.circle(self.surface, (150, 0, 0), self.pos, self.radius2)
