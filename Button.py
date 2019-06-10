# Use this class to make buttons
import pygame


class Button:
    def __init__(self, surface, pos, size, color=(0, 0, 0), img=''):
        self.color = color
        self.pos = pos
        self.size = size
        self.surface = surface
        self.rect = (self.pos[0], self.pos[1], self.size[0], self.size[1])
        self.sprite = None

        if img == '':
            pygame.draw.rect(self.surface, self.color, self.rect)
        else:
            self.sprite = pygame.image.load(img)

    def draw(self):
        if self.sprite is None:
            pygame.draw.rect(self.surface, self.color, self.rect)
        else:
            self.surface.blit(self.sprite, self.pos)