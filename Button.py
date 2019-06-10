# Use this class to make buttons
import pygame


class Button:
    def __init__(self, surface, pos, size, id, img='', color=(0, 0, 0)):
        self.color = color
        self.pos = pos
        self.size = size
        self.surface = surface
        self.rect = (self.pos[0], self.pos[1], self.size[0], self.size[1])
        self.sprite = None
        self.id = id

        if img == '':
            pygame.draw.rect(self.surface, self.color, self.rect)
        else:
            self.sprite = pygame.image.load(img)

    def draw(self):
        if self.sprite is None:
            pygame.draw.rect(self.surface, self.color, self.rect)
        else:
            self.surface.blit(self.sprite, self.pos)

    def get_click(self):
        if self.pos[0] <= pygame.mouse.get_pos()[0] < self.pos[0] + self.size[0] and self.pos[1] <= pygame.mouse.get_pos()[1] < self.pos[1] + self.size[1] and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False

    def get_id(self):
        return self.id