# This file is used to make the menu #
import pygame
from TextFile import *


class Menu:
    def __init__(self):
        self.screen_dim = (800, 600)
        self.display = pygame.display.set_mode(self.screen_dim)
        self.instruction = Text("Type the Server Name:", self.display)
        self.instruction.set_pos((400 - self.instruction.get_size()[0]/2, 150))
        self.text_back = Background((150, 150, 150), (400, 55), (200, 160 + self.instruction.get_size()[1]), self.display)

    def run_menu(self):
        pygame.init()
        run = True
        while run:
            for event in pygame.event.get():  # Returns all inputs and triggers into an array
                if event.type == pygame.QUIT:  # If the red X was clicked
                    run = False

            self.display.fill((255, 255, 255))

            self.instruction.draw()
            self.text_back.draw()

            pygame.display.update()
        pygame.quit()