# This file creates the endscreen #
from Mixer import *
from TextFile import *


class Endscreen:
    def __init__(self, song, status):
        color = {
            "You Win": (0, 255, 0),
            "You Suck": (255, 0, 0)
        }
        self.screen_dim = (800, 600)
        self.display = pygame.display.set_mode(self.screen_dim)
        self.song_name = song
        self.music = Music()
        self.music.set_sound(self.song_name)
        self.status = Text(status, self.display) # Win, lose, or tie
        self.status.set_size(80)
        self.status.set_pos((400 - (self.status.get_size()[0])/2, 300 - (self.status.get_size()[1])/2))
        self.text_back = Background(color[status], (self.status.get_size()[0] + 30, self.status.get_size()[1] + 30), (400 - (self.status.get_size()[0] + 30)/2, 300 - (self.status.get_size()[1] + 30)/2), self.display)

    def run_endscreen(self):
        pygame.init()
        self.music.play(-1)
        run = True
        while run:
            for event in pygame.event.get():  # Returns all inputs and triggers into an array
                if event.type == pygame.QUIT:  # If the red X was clicked
                    run = False

            self.display.fill((255, 255, 255))

            # Draw Sprites #
            self.text_back.draw()
            self.status.draw()

            pygame.display.update()
