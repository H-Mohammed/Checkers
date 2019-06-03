# This file creates the endscreen #
import pygame


class Endscreen:
    def __init__(self):
        self.screen_dim = (800, 600)
        self.display = pygame.display.set_mode(self.screen_dim)

    def run_endscreen(self):
        pygame.init()
        run = True
        while run:
            for event in pygame.event.get():  # Returns all inputs and triggers into an array
                if event.type == pygame.QUIT:  # If the red X was clicked
                    run = False
