# This file contains classes that make individual objects #
import pygame


class Objects:  # This is the parent class used to make any objects
    def __init__(self, surface, color, pos):
        self.color = color
        self.pos = pos
        self.surface = surface
        self.x = pos[0]
        self.y = pos[1]
    
    def getx(self):
        return self.x
    
    def gety(self):
        return self.y


class Checker(Objects):  # This is used to make the checker pieces
    def __init__(self, surface, color, pos):
        super().__init__(surface, color, pos)
        self.radius = 30
        pygame.draw.circle(self.surface, self.color, (self.x + 30, self.y + 30), self.radius)
        self.crown = 0

    def draw(self):
        pygame.draw.circle(self.surface, self.color, (self.x + 30, self.y + 30), self.radius)
    
    def get_height(self):
        return self.radius*2
    
    def get_width(self):
        return self.radius*2
    
    def setPos(self,pos):
        self.x = pos[0]
        self.y = pos[1]
    
    def pos_movement(self, pieces, enemy, mouse_pos, mouse_pressed):
        star = Star(self.surface, 'media/Star.png', (0, 0))  # Create the star
        top_right = 0
        top_left = 0
        bottom_right = 0
        bottom_left = 0
        for item in pieces:
            if item.gety() == self.gety() + 60:
                if item.getx() == self.getx() + 60:
                    bottom_right = 1
                if item.getx() == self.getx() - 60:
                    bottom_left = 1
            if item.gety() == self.gety() - 60:
                if item.getx() == self.getx() + 60:
                    top_right = 1
                if item.getx() == self.getx() - 60:
                    top_left = 1

        for item in enemy:
            if item.gety() == self.gety() + 60:
                if item.getx() == self.getx() + 60:
                    bottom_right = 2
                    enemy1 = item
                        
                if item.getx() == self.getx() - 60:
                    bottom_left = 2
                    enemy2 = item
            if item.gety() == self.gety() - 60:
                if item.getx() == self.getx() + 60:
                    top_right = 2
                    enemy3 = item
                if item.getx() == self.getx() - 60:
                    top_left = 2
                    enemy4 = item
        for item in enemy:
            if bottom_right == 2:
                if item.gety() == self.gety() + 120:
                    if item.getx() == self.getx() + 120:
                        bottom_right = 3
            if bottom_left == 2:
                if item.gety() == self.gety() + 120:
                    if item.getx() == self.getx() - 120:
                        bottom_left = 3
            if top_left == 2:
                if item.gety() == self.gety() - 120:
                    if item.getx() == self.getx() - 120:
                        top_left = 3
            if top_right == 2:
                if item.gety() == self.gety() - 120:
                    if item.getx() == self.getx() + 120:
                        top_right = 3
            
        if self.getx()+60 >= 8*60 and top_right == 0:
            top_right = 1
        if self.getx()+120 >= 8*60 and top_right == 2:
            top_right = 3
        if self.getx()-60 < 0 and top_left == 0:
            top_left = 1
        if self.getx()-120 < 0 and top_left == 2:
            top_left = 3
        if self.getx()-60 < 0 and bottom_left == 0:
            bottom_left = 1
        if self.getx()-120 < 0 and bottom_left == 2:
            bottom_left = 3
        if self.getx()+60 >= 8*60 and bottom_right == 0:
            bottom_right = 1
        if self.getx()+120 >= 8*60 and bottom_right == 2:
            bottom_right = 3

        if top_left == 0:
            star.set_pos((self.getx() - 60, self.gety() - 60))
            star.draw()
            if self.getx()-60 <= mouse_pos[0] <= self.getx() and self.gety()-60 <= mouse_pos[1] <= self.gety():
                if mouse_pressed[0] == 1:
                    self.setPos((self.getx()-60,self.gety()-60))
                    self.draw()
                    del star
                    return 1
        if top_right == 0:
            star.set_pos((self.getx() + 60, self.gety() - 60))
            star.draw()
            if self.getx()+60 <= mouse_pos[0] <= self.getx()+120 and self.gety()-60 <= mouse_pos[1] <= self.gety():
                if mouse_pressed[0] == 1:
                    self.setPos((self.getx()+60,self.gety()-60))
                    self.draw()
                    del star
                    return 1
        if bottom_left == 0:
            star.set_pos((self.getx() - 60, self.gety() + 60))
            star.draw()
            if self.getx()-60 <= mouse_pos[0] <= self.getx() and self.gety()+60 <= mouse_pos[1] <= self.gety()+120:
                if mouse_pressed[0] == 1:
                    self.setPos((self.getx()-60,self.gety()+60))
                    self.draw()
                    del star
                    return 1
        if bottom_right == 0:
            star.set_pos((self.getx() + 60, self.gety() + 60))
            star.draw()
            if self.getx()+60 <= mouse_pos[0] <= self.getx()+120 and self.gety()+60 <= mouse_pos[1] <= self.gety()+120:
                if mouse_pressed[0] == 1:
                    self.setPos((self.getx()+60,self.gety()+60))
                    self.draw()
                    del star
                    return 1
        
        if top_left == 2:
            star.set_pos((self.getx() - 120, self.gety() - 120))
            star.draw()
            if self.getx()-120 <= mouse_pos[0] <= self.getx()-60 and self.gety()-120 <= mouse_pos[1] <= self.gety()-60:
                if mouse_pressed[0] == 1:
                    self.setPos((self.getx()-120,self.gety()-120))
                    self.draw()
                    
                    enemy.pop(enemy.index(enemy4))
                    del enemy4
                    del star
                    return 1
        if top_right == 2:
            star.set_pos((self.getx() + 120, self.gety() - 120))
            star.draw()
            if self.getx()+120 <= mouse_pos[0] <= self.getx()+180 and self.gety()-120 <= mouse_pos[1] <= self.gety()-60:
                if mouse_pressed[0] == 1:
                    self.setPos((self.getx()+120,self.gety()-120))
                    self.draw()
                    
                    enemy.pop(enemy.index(enemy3))
                    del enemy3
                    del star
                    return 1
        if bottom_left == 2:
            star.set_pos((self.getx() - 120, self.gety() + 120))
            star.draw()
            if self.getx()-120 <= mouse_pos[0] <= self.getx()-60 and self.gety()+120 <= mouse_pos[1] <= self.gety()+180:
                if mouse_pressed[0] == 1:
                    self.setPos((self.getx()-120,self.gety()+120))
                    self.draw()
                    
                    enemy.pop(enemy.index(enemy2))
                    del enemy2
                    del star
                    return 1
        if bottom_right == 2:
            star.set_pos((self.getx() + 120, self.gety() + 120))
            star.draw()
            if self.getx()+120 <= mouse_pos[0] <= self.getx()+180 and self.gety()+120 <= mouse_pos[1] <= self.gety()+180:
                if mouse_pressed[0] == 1:
                    self.setPos((self.getx()+120,self.gety()+120))
                    self.draw()
                    enemy.pop(enemy.index(enemy1))
                    del enemy1
                    del star
                    return 1
        

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
    def __init__(self, window, filename, pos):
        super().__init__(window, (0, 0, 0), pos)
        self.sprite = pygame.image.load(filename).convert_alpha()
        self.pos = pos
    
    def draw(self):
        self.surface.blit(self.sprite, self.pos)

    def set_pos(self, pos):
        self.pos = pos
