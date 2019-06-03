# This file contains classes that make individual objects #
import pygame


class Objects:  # This is the parent class used to make any objects
    def __init__(self, surface, color, pos):
        self.color = color
        self.pos = pos
        self.surface = surface
        self.x = pos[0]
        self.y = pos[1]

    def get_pos(self):
        return self.pos
    
    def getx(self):
        return self.x
    
    def gety(self):
        return self.y

    def set_pos(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.pos = pos


class Checker(Objects):  # This is used to make the checker pieces
    def __init__(self, surface, color, pos, num):
        super().__init__(surface, color, pos)
        self.radius = 30
        self.crown = 0
        self.id = num

    def draw(self):
        pygame.draw.circle(self.surface, self.color, (self.x + 30, self.y + 30), self.radius)
    
    def get_height(self):
        return self.radius*2
    
    def get_width(self):
        return self.radius*2
    
    def get_id(self):
        return self.id
    
    def checkCapture(self, enemy, pieces):  # Checks if the piece can capture
        testBR = 0  # Tests if there is a piece on Bottom Right
        testBL = 0  # Tests if there is a piece on Bottom Left
        testTR = 0  # Tests if there is a piece on Top Right
        testTL = 0  # Tests if there is a piece on Top Left
        # --- Tests if there is a piece 1 unit diagonally --- #
        for item in enemy:
            if self.crown == 1:
                if item.gety() == self.gety() + 60:
                    if item.getx() == self.getx() + 60:
                        testBR = 1
                    if item.getx() == self.getx() - 60:
                        testBL = 1
            if item.gety() == self.gety() - 60:
                if item.getx() == self.getx() + 60:
                    testTR = 1
                if item.getx() == self.getx() - 60:
                    testTL = 1
        # --- Tests if there is a piece 2 units diagonally --- #
        for item in enemy:
            if item.gety() == self.gety() + 120 and testBR == 1:
                if item.getx() == self.getx() + 120:
                    testBR = 0
            
            if item.gety() == self.gety() + 120 and testBL == 1:
                if item.getx() == self.getx() - 120:
                    testBL = 0
            if item.gety() == self.gety() - 120 and testTL == 1:
                if item.getx() == self.getx() - 120:
                    testTL = 0
            if item.gety() == self.gety() - 120 and testTR == 1:
                if item.getx() == self.getx() + 120:
                    testTR = 0

        for item in pieces:
            if item.gety() == self.gety() + 120 and testBR == 1:
                if item.getx() == self.getx() + 120:
                    testBR = 0
            
            if item.gety() == self.gety() + 120 and testBL == 1:
                if item.getx() == self.getx() - 120:
                    testBL = 0
            if item.gety() == self.gety() - 120 and testTL == 1:
                if item.getx() == self.getx() - 120:
                    testTL = 0
            if item.gety() == self.gety() - 120 and testTR == 1:
                if item.getx() == self.getx() + 120:
                    testTR = 0

        # --- Checks if move is out of bounds --- #
        if (self.gety() + 120 >= 480 or self.getx() + 120 >= 480) and testBR == 1:
            testBR = 0
        if (self.gety() + 120 >= 480 or self.getx() - 120 <= 0) and testBL == 1:
            testBL = 0
        if (self.gety() - 120 <= 0 or self.getx() + 120 >= 480) and testTR == 1:
            testTR = 0
        if (self.gety() - 120 <= 0 or self.getx() - 120 <= 0) and testTL == 1:
            testTL = 0
        if testBL == 1 or testBR == 1 or testTL == 1 or testTR == 1:
            return True
        else:
            return False

    def pos_movement(self, pieces, enemy, mouse_pos, mouse_pressed,color):
        star = Star(self.surface, 'media/Star.png', (0, 0))  # Create the star
        top_right = 0
        top_left = 0
        bottom_right = 0
        bottom_left = 0
        capture = 0
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
            if self.crown == 1 or not color == 0:
                if item.gety() == self.gety() + 60:
                    if item.getx() == self.getx() + 60:
                        bottom_right = 2
                        enemy1 = item
                            
                    if item.getx() == self.getx() - 60:
                        bottom_left = 2
                        enemy2 = item
            if not color == 1 or self.crown == 1:
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
        for item in pieces:
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
        
        for item in pieces:
            if item.checkCapture(enemy,pieces):
                capture = 1
                break
            
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

        if self.gety()+60 >= 8*60 and bottom_left == 0:
            bottom_left = 1
        if self.gety()+120 >= 8*60 and bottom_left == 2:
            bottom_left = 3
        if self.gety()+60 >= 8*60 and bottom_right == 0:
            bottom_right = 1
        if self.gety()+120 >= 8*60 and bottom_right == 2:
            bottom_right = 3
        if self.gety()-60 < 0 and top_left == 0:
            top_left = 1
        if self.gety()-120 < 0 and top_left == 2:
            top_left = 3
        if self.gety()-60 < 0 and top_right == 0:
            top_right = 1
        if self.gety()-120 < 0 and top_right == 2:
            top_right = 3
        
        
        if color == 0:
            
            if not (top_left == 2 or top_right == 2 or bottom_left == 2 or bottom_right == 2) and capture == 0:
                if top_left == 0:
                    star.set_pos((self.getx() - 60, self.gety() - 60))
                    star.draw()
                    if self.getx()-60 <= mouse_pos[0] <= self.getx() and self.gety()-60 <= mouse_pos[1] <= self.gety():
                        if mouse_pressed[0] == 1:
                            self.set_pos((self.getx()-60,self.gety()-60))
                            self.draw()
                            del star
                            return 1
                if top_right == 0:
                    star.set_pos((self.getx() + 60, self.gety() - 60))
                    star.draw()
                    if self.getx()+60 <= mouse_pos[0] <= self.getx()+120 and self.gety()-60 <= mouse_pos[1] <= self.gety():
                        if mouse_pressed[0] == 1:
                            self.set_pos((self.getx()+60,self.gety()-60))
                            self.draw()
                            del star
                            return 1
                if self.crown == 1:
                    if bottom_left == 0:
                        star.set_pos((self.getx() - 60, self.gety() + 60))
                        star.draw()
                        if self.getx()-60 <= mouse_pos[0] <= self.getx() and self.gety()+60 <= mouse_pos[1] <= self.gety()+120:
                            if mouse_pressed[0] == 1:
                                self.set_pos((self.getx()-60,self.gety()+60))
                                self.draw()
                                del star
                                return 1
                    if bottom_right == 0:
                        star.set_pos((self.getx() + 60, self.gety() + 60))
                        star.draw()
                        if self.getx()+60 <= mouse_pos[0] <= self.getx()+120 and self.gety()+60 <= mouse_pos[1] <= self.gety()+120:
                            if mouse_pressed[0] == 1:
                                self.set_pos((self.getx()+60,self.gety()+60))
                                self.draw()
                                del star
                                return 1
            
            if top_left == 2:
                star.set_pos((self.getx() - 120, self.gety() - 120))
                star.draw()
                if self.getx()-120 <= mouse_pos[0] <= self.getx()-60 and self.gety()-120 <= mouse_pos[1] <= self.gety()-60:
                    if mouse_pressed[0] == 1:
                        self.set_pos((self.getx()-120,self.gety()-120))
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
                        self.set_pos((self.getx()+120,self.gety()-120))
                        self.draw()
                        enemy.pop(enemy.index(enemy3))
                        del enemy3
                        del star
                        return 1
            if self.crown == 1:
                if bottom_left == 2:
                    star.set_pos((self.getx() - 120, self.gety() + 120))
                    star.draw()
                    if self.getx()-120 <= mouse_pos[0] <= self.getx()-60 and self.gety()+120 <= mouse_pos[1] <= self.gety()+180:
                        if mouse_pressed[0] == 1:
                            self.set_pos((self.getx()-120,self.gety()+120))
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
                            self.set_pos((self.getx()+120,self.gety()+120))
                            self.draw()
                            enemy.pop(enemy.index(enemy1))
                            del enemy1
                            del star
                            return 1
            if self.gety() == 0:
                self.crown = 1
                        
        if color == 1:
            
            if not (top_left == 2 or top_right == 2 or bottom_left == 2 or bottom_right == 2) and capture == 0:
                if self.crown == 1:
                    if top_left == 0:
                        star.set_pos((self.getx() - 60, self.gety() - 60))
                        star.draw()
                        if self.getx()-60 <= mouse_pos[0] <= self.getx() and self.gety()-60 <= mouse_pos[1] <= self.gety():
                            if mouse_pressed[0] == 1:
                                self.set_pos((self.getx()-60,self.gety()-60))
                                self.draw()
                                del star
                                return 1
                    
                    if top_right == 0:
                        star.set_pos((self.getx() + 60, self.gety() - 60))
                        star.draw()
                        if self.getx()+60 <= mouse_pos[0] <= self.getx()+120 and self.gety()-60 <= mouse_pos[1] <= self.gety():
                            if mouse_pressed[0] == 1:
                                self.set_pos((self.getx()+60,self.gety()-60))
                                self.draw()
                                del star
                                return 1
                if bottom_left == 0:
                    star.set_pos((self.getx() - 60, self.gety() + 60))
                    star.draw()
                    if self.getx()-60 <= mouse_pos[0] <= self.getx() and self.gety()+60 <= mouse_pos[1] <= self.gety()+120:
                        if mouse_pressed[0] == 1:
                            self.set_pos((self.getx()-60,self.gety()+60))
                            self.draw()
                            del star
                            return 1
                if bottom_right == 0:
                    star.set_pos((self.getx() + 60, self.gety() + 60))
                    star.draw()
                    if self.getx()+60 <= mouse_pos[0] <= self.getx()+120 and self.gety()+60 <= mouse_pos[1] <= self.gety()+120:
                        if mouse_pressed[0] == 1:
                            self.set_pos((self.getx()+60,self.gety()+60))
                            self.draw()
                            del star
                            return 1
            if self.crown == 1:
                if top_left == 2:
                    star.set_pos((self.getx() - 120, self.gety() - 120))
                    star.draw()
                    if self.getx()-120 <= mouse_pos[0] <= self.getx()-60 and self.gety()-120 <= mouse_pos[1] <= self.gety()-60:
                        if mouse_pressed[0] == 1:
                            self.set_pos((self.getx()-120,self.gety()-120))
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
                            self.set_pos((self.getx()+120,self.gety()-120))
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
                        self.set_pos((self.getx()-120,self.gety()+120))
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
                        self.set_pos((self.getx()+120,self.gety()+120))
                        self.draw()
                        enemy.pop(enemy.index(enemy1))
                        del enemy1
                        del star
                        return 1
            if self.gety() == 7*60:
                self.crown = 1
        

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
