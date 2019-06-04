# This file creates the endscreen #
from Mixer import *


class Endscreen:
    def __init__(self, song):
        self.screen_dim = (800, 600)
        self.display = pygame.display.set_mode(self.screen_dim)
        self.song_name = song
        self.music = Music()
        self.music.set_sound(self.song_name)

    def run_endscreen(self):
        pygame.init()
        self.music.play(-1)
        run = True
        while run:
            for event in pygame.event.get():  # Returns all inputs and triggers into an array
                if event.type == pygame.QUIT:  # If the red X was clicked
                    run = False

            self.display.fill((255, 255, 255))

            pygame.display.update()
