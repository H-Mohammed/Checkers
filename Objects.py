# This file contains classes that make individual objects #
import pygame


class Objects:  # This is the parent class used to make any objects
    def __init__(self, surface, color, pos):
        self.color = color
        self.pos = pos
        self.surface = surface
        self.x = pos[0]
        self.y = pos[1]
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y


class Checker(Objects):  # This is used to make the checker pieces
    def __init__(self, surface, color, pos):
        super().__init__(surface, color, pos)
        self.radius = 30
        pygame.draw.circle(self.surface, self.color, (self.x + 30, self.y + 30), self.radius)

    def draw(self):
        pygame.draw.circle(self.surface, self.color, (self.x + 30, self.y + 30), self.radius)
    
    def getHeight(self):
        return self.radius*2
    
    def getWidth(self):
        return self.radius*2
    
    def posMovement(self, pieces, enemy):
        star = Star(self.surface, 'media/Star.png', (0, 0))  # Create the star
        for item in pieces:
            if not item.getX() == self.getX()+60:
                if not item.getY() == self.getY()+60:
                    star.setPos((self.getX() + 60, self.getY() + 60))
                    star.draw()
                if not item.getY() == self.getY()-60:
                    star.setPos((self.getX() + 60, self.getY() - 60))
                    star.draw()
            if not item.getX() == self.getX()-60:
                if not item.getY() == self.getY()+60:
                    star.setPos((self.getX() - 60, self.getY() + 60))
                    star.draw()
                if not item.getY() == self.getY()-60:
                    star.setPos((self.getX()-60,self.getY()-60))
                    star.draw()
        for item in enemy:
            if item.getX() == self.getX()+60:
                if item.getY() == self.getY()+60:
                    star.setPos((self.getX()+120,self.getY()+120))
                    star.draw()
                if item.getY() == self.getY()-60:
                    star.setPos((self.getX()+120,self.getY()-120))
                    star.draw()
            if item.getX() == self.getX()-60:
                if item.getY() == self.getY()+60:
                    star.setPos((self.getX()-120,self.getY()+120))
                    star.draw()
                if item.getY() == self.getY()-60:
                    star.setPos((self.getX()-120,self.getY()-120))
                    star.draw()
            
                


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

class Star(Objects):
    def __init__(self, window, fileName, pos):
        super().__init__(window, (0, 0, 0), pos)
        self.sprite = pygame.image.load(fileName).convert_alpha()
        self.pos = pos
    
    def draw(self):
        self.surface.blit(self.sprite, self.pos)

    def setPos(self, pos):
        self.pos = pos
