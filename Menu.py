# This file is used to make the menu #
import pygame
from TextFile import *


class Menu:
    def __init__(self):
        self.screen_dim = (800, 600)
        self.display = pygame.display.set_mode(self.screen_dim)
        self.text1 = Text("Type the Server Name", self.display)

    def run_menu(self):
        pygame.init()
        run = True
        while run:
            for event in pygame.event.get():  # Returns all inputs and triggers into an array
                if event.type == pygame.QUIT:  # If the red X was clicked
                    run = False

            self.text1.draw()

            self.display.fill((255, 255, 255))
            pygame.display.update()
        pygame.quit()