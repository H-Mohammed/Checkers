# This file creates the endscreen #
import pygame


class Endscreen:
    def __init__(self):
        self.screen_dim = (800, 600)
        self.display = pygame.display.set_mode(self.screen_dim)