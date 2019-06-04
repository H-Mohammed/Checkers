# This file contains classes that make individual objects #
from Mixer import *


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
        if self.color == (0, 0, 0):
            self.sprite = pygame.image.load('media/whiteking.png')
        else:
            self.sprite = pygame.image.load('media/blackking.png')

    def draw(self):
        pygame.draw.circle(self.surface, self.color, (self.x + 30, self.y + 30), self.radius)
        if self.crown == 1:
            self.surface.blit(self.sprite, (self.x, self.y))

    def get_height(self):
        return self.radius*2

    def get_width(self):
        return self.radius*2

    def get_id(self):
        return self.id
    
    def checkMovement(self,enemy,pieces,color):
        top_right = 0
        top_left = 0
        bottom_right = 0
        bottom_left = 0
        # --- Checks if diagonal is occupied by a friendly piece --- #
        # 1 means diagonal is occupied #
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

        # --- Checks if there is an enemy at each diagonal --- #
        # 2 means there is an enemy piece at diagonal #
        for item in enemy:
            if self.crown == 1 or color == 1:
                if item.gety() == self.gety() + 60:
                    if item.getx() == self.getx() + 60:
                        bottom_right = 2
                        enemy1 = item
                    if item.getx() == self.getx() - 60:
                        bottom_left = 2
                        enemy2 = item
            if color == 0 or self.crown == 1:
                if item.gety() == self.gety() - 60:
                    if item.getx() == self.getx() + 60:
                        top_right = 2
                        enemy3 = item
                    if item.getx() == self.getx() - 60:
                        top_left = 2
                        enemy4 = item
        # --- Checks if enemy piece cannot be captured --- #
        # 3 means it CANNOT be captured #
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
        # --- Check if move is out of bounds --- #
        # x-coordinate #
        if self.getx() + 60 >= 480 and top_right == 0:
            top_right = 1
        if self.getx() + 120 >= 480 and top_right == 2:
            top_right = 3
        if self.getx() - 60 < 0 and top_left == 0:
            top_left = 1
        if self.getx() - 120 < 0 and top_left == 2:
            top_left = 3
        if self.getx() - 60 < 0 and bottom_left == 0:
            bottom_left = 1
        if self.getx() - 120 < 0 and bottom_left == 2:
            bottom_left = 3
        if self.getx() + 60 >= 480 and bottom_right == 0:
            bottom_right = 1
        if self.getx() + 120 >= 480 and bottom_right == 2:
            bottom_right = 3
        # y-coordinate #
        if self.gety() + 60 >= 480 and bottom_left == 0:
            bottom_left = 1
        if self.gety() + 120 >= 480 and bottom_left == 2:
            bottom_left = 3
        if self.gety() + 60 >= 480 and bottom_right == 0:
            bottom_right = 1
        if self.gety() + 120 >= 480 and bottom_right == 2:
            bottom_right = 3
        if self.gety() - 60 < 0 and top_left == 0:
            top_left = 1
        if self.gety() - 120 < 0 and top_left == 2:
            top_left = 3
        if self.gety() - 60 < 0 and top_right == 0:
            top_right = 1
        if self.gety() - 120 < 0 and top_right == 2:
            top_right = 3
        
        if top_right == 0 or top_right == 2 or top_left == 0 or top_left == 2 or bottom_right == 0 or bottom_right == 2 or bottom_left == 0 or bottom_left == 2:
            return 1
        else:
            return 0

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
        print(testBR,testBL,testTR,testTL)
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
        print(testBR, testBL, testTR, testTL)
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
        print(testBR, testBL, testTR, testTL)
        # --- Checks if move is out of bounds --- #
        if (self.gety() + 120 >= 480 or self.getx() + 120 >= 480) and testBR == 1:
            testBR = 0
        if (self.gety() + 120 >= 480 or self.getx() - 120 < 0) and testBL == 1:
            testBL = 0
        if (self.gety() - 120 < 0 or self.getx() + 120 >= 480) and testTR == 1:
            testTR = 0
        if (self.gety() - 120 < 0 or self.getx() - 120 < 0) and testTL == 1:
            testTL = 0
        print(testBR, testBL, testTR, testTL)
        #print('Test: ' + str(testTL), str(testTR), str(testBL), str(testBR))
        if testBL == 1 or testBR == 1 or testTL == 1 or testTR == 1:
            return True
        else:
            return False

    def pos_movement(self, pieces, enemy, mouse_pos, mouse_pressed,color):
        star = Star(self.surface, 'media/Star.png', (0, 0))  # Create the star
        music = Music()
        music.set_sound('checker_sound_effect')
        top_right = 0
        top_left = 0
        bottom_right = 0
        bottom_left = 0
        capture = 0
        # --- Checks if diagonal is occupied by a friendly piece --- #
        # 1 means diagonal is occupied #
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

        # --- Checks if there is an enemy at each diagonal --- #
        # 2 means there is an enemy piece at diagonal #
        for item in enemy:
            if self.crown == 1 or color == 1:
                if item.gety() == self.gety() + 60:
                    if item.getx() == self.getx() + 60:
                        bottom_right = 2
                        enemy1 = item
                    if item.getx() == self.getx() - 60:
                        bottom_left = 2
                        enemy2 = item
            if color == 0 or self.crown == 1:
                if item.gety() == self.gety() - 60:
                    if item.getx() == self.getx() + 60:
                        top_right = 2
                        enemy3 = item
                    if item.getx() == self.getx() - 60:
                        top_left = 2
                        enemy4 = item
        # --- Checks if enemy piece cannot be captured --- #
        # 3 means it CANNOT be captured #
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
        # --- Check if an enemy can be captured --- #
        for item in pieces:
            if item.checkCapture(enemy, pieces):
                capture = 1  # Player will be forced to capture
                break
        # --- Check if move is out of bounds --- #
        # x-coordinate #
        if self.getx() + 60 >= 480 and top_right == 0:
            top_right = 1
        if self.getx() + 120 >= 480 and top_right == 2:
            top_right = 3
        if self.getx() - 60 < 0 and top_left == 0:
            top_left = 1
        if self.getx() - 120 < 0 and top_left == 2:
            top_left = 3
        if self.getx() - 60 < 0 and bottom_left == 0:
            bottom_left = 1
        if self.getx() - 120 < 0 and bottom_left == 2:
            bottom_left = 3
        if self.getx() + 60 >= 480 and bottom_right == 0:
            bottom_right = 1
        if self.getx() + 120 >= 480 and bottom_right == 2:
            bottom_right = 3
        # y-coordinate #
        if self.gety() + 60 >= 480 and bottom_left == 0:
            bottom_left = 1
        if self.gety() + 120 >= 480 and bottom_left == 2:
            bottom_left = 3
        if self.gety() + 60 >= 480 and bottom_right == 0:
            bottom_right = 1
        if self.gety() + 120 >= 480 and bottom_right == 2:
            bottom_right = 3
        if self.gety() - 60 < 0 and top_left == 0:
            top_left = 1
        if self.gety() - 120 < 0 and top_left == 2:
            top_left = 3
        if self.gety() - 60 < 0 and top_right == 0:
            top_right = 1
        if self.gety() - 120 < 0 and top_right == 2:
            top_right = 3
        #print(top_left, top_right, bottom_left, bottom_right)
        # --- Display where the player can MOVE a piece --- #
        if color == 0:  # Bottom Player
            # Check if player cannot capture #
            if not (top_left == 2 or top_right == 2 or bottom_left == 2 or bottom_right == 2) and capture == 0:
                if top_left == 0:
                    star.set_pos((self.getx() - 60, self.gety() - 60))
                    star.draw()
                    # Move piece when mouse click event is detected #
                    if self.getx() - 60 <= mouse_pos[0] <= self.getx() and self.gety() - 60 <= mouse_pos[1] <= self.gety():
                        if mouse_pressed[0] == 1:
                            self.set_pos((self.getx() - 60, self.gety() - 60))
                            self.draw()
                            music.play()
                            del star
                            return 1
                if top_right == 0:
                    star.set_pos((self.getx() + 60, self.gety() - 60))
                    star.draw()
                    # Move piece when mouse click event is detected #
                    if self.getx() + 60 <= mouse_pos[0] <= self.getx() + 120 and self.gety() - 60 <= mouse_pos[1] <= self.gety():
                        if mouse_pressed[0] == 1:
                            self.set_pos((self.getx() + 60, self.gety() - 60))
                            self.draw()
                            music.play()
                            del star
                            return 1
                if self.crown == 1:
                    if bottom_left == 0:
                        star.set_pos((self.getx() - 60, self.gety() + 60))
                        star.draw()
                        # Move piece when mouse click event is detected #
                        if self.getx()-60 <= mouse_pos[0] <= self.getx() and self.gety()+60 <= mouse_pos[1] <= self.gety()+120:
                            if mouse_pressed[0] == 1:
                                self.set_pos((self.getx()-60,self.gety()+60))
                                self.draw()
                                music.play()
                                del star
                                return 1
                    if bottom_right == 0:
                        star.set_pos((self.getx() + 60, self.gety() + 60))
                        star.draw()
                        # Move piece when mouse click event is detected #
                        if self.getx()+60 <= mouse_pos[0] <= self.getx()+120 and self.gety()+60 <= mouse_pos[1] <= self.gety()+120:
                            if mouse_pressed[0] == 1:
                                self.set_pos((self.getx()+60,self.gety()+60))
                                self.draw()
                                music.play()
                                del star
                                return 1
            # Check if player can capture top left #
            if top_left == 2:
                star.set_pos((self.getx() - 120, self.gety() - 120))
                star.draw()
                if self.getx()-120 <= mouse_pos[0] <= self.getx()-60 and self.gety()-120 <= mouse_pos[1] <= self.gety()-60:
                    if mouse_pressed[0] == 1:
                        self.set_pos((self.getx()-120,self.gety()-120))
                        self.draw()
                        music.play()
                        enemy.pop(enemy.index(enemy4))
                        del enemy4
                        del star
                        while self.checkCapture(enemy, pieces):
                            print("It goes here")
                            return self.pos_movement(pieces,enemy,pygame.mouse.get_pos(), pygame.mouse.get_pressed(), color)
                        return 1
            # Check if player can capture top right #
            if top_right == 2:
                star.set_pos((self.getx() + 120, self.gety() - 120))
                star.draw()
                if self.getx()+120 <= mouse_pos[0] <= self.getx()+180 and self.gety()-120 <= mouse_pos[1] <= self.gety()-60:
                    if mouse_pressed[0] == 1:
                        self.set_pos((self.getx()+120,self.gety()-120))
                        self.draw()
                        music.play()
                        enemy.pop(enemy.index(enemy3))
                        del enemy3
                        del star
                        if self.checkCapture(enemy, pieces):
                            print("It goes here")
                            return self.pos_movement(pieces,enemy,mouse_pos, mouse_pressed, color)
                        return 1
            if self.crown == 1:
                # Check if player can capture bottom left #
                if bottom_left == 2:
                    star.set_pos((self.getx() - 120, self.gety() + 120))
                    star.draw()
                    if self.getx()-120 <= mouse_pos[0] <= self.getx()-60 and self.gety()+120 <= mouse_pos[1] <= self.gety()+180:
                        if mouse_pressed[0] == 1:
                            self.set_pos((self.getx()-120,self.gety()+120))
                            self.draw()
                            music.play()
                            enemy.pop(enemy.index(enemy2))
                            del enemy2
                            del star
                            if self.checkCapture(enemy, pieces):
                                print("It goes here")
                                return self.pos_movement(pieces,enemy,mouse_pos, mouse_pressed, color)
                            return 1
                # Check if player can capture bottom right
                if bottom_right == 2:
                    star.set_pos((self.getx() + 120, self.gety() + 120))
                    star.draw()
                    if self.getx()+120 <= mouse_pos[0] <= self.getx()+180 and self.gety()+120 <= mouse_pos[1] <= self.gety()+180:
                        if mouse_pressed[0] == 1:
                            self.set_pos((self.getx()+120,self.gety()+120))
                            self.draw()
                            music.play()
                            enemy.pop(enemy.index(enemy1))
                            del enemy1
                            del star
                            if self.checkCapture(enemy, pieces):
                                print("It goes here")
                                return self.pos_movement(pieces,enemy,mouse_pos, mouse_pressed, color)
                            return 1
            # Check if piece made it to the top of the board #
            if self.gety() == 0:
                self.crown = 1

        if color == 1:  # Top Player
            # Check if player cannot capture #
            if not (top_left == 2 or top_right == 2 or bottom_left == 2 or bottom_right == 2):
                if self.crown == 1:
                    if top_left == 0:
                        star.set_pos((self.getx() - 60, self.gety() - 60))
                        star.draw()
                        # Move piece when mouse click event is detected #
                        if self.getx() - 60 <= mouse_pos[0] <= self.getx() and self.gety() - 60 <= mouse_pos[1] <= self.gety():
                            if mouse_pressed[0] == 1:
                                self.set_pos((self.getx() - 60, self.gety() - 60))
                                self.draw()
                                music.play()
                                del star
                                return 1

                    if top_right == 0:
                        star.set_pos((self.getx() + 60, self.gety() - 60))
                        star.draw()
                        # Move piece when mouse click event is detected #
                        if self.getx()+60 <= mouse_pos[0] <= self.getx()+120 and self.gety()-60 <= mouse_pos[1] <= self.gety():
                            if mouse_pressed[0] == 1:
                                self.set_pos((self.getx() + 60, self.gety() - 60))
                                self.draw()
                                music.play()
                                del star
                                return 1
                if bottom_left == 0:
                    star.set_pos((self.getx() - 60, self.gety() + 60))
                    star.draw()
                    # Move piece when mouse click event is detected #
                    if self.getx() - 60 <= mouse_pos[0] <= self.getx() and self.gety() + 60 <= mouse_pos[1] <= self.gety() + 120:
                        if mouse_pressed[0] == 1:
                            self.set_pos((self.getx() - 60, self.gety() + 60))
                            self.draw()
                            music.play()
                            del star
                            return 1
                if bottom_right == 0:
                    star.set_pos((self.getx() + 60, self.gety() + 60))
                    star.draw()
                    # Move piece when mouse click event is detected #
                    if self.getx() + 60 <= mouse_pos[0] <= self.getx() + 120 and self.gety() + 60 <= mouse_pos[1] <= self.gety() + 120:
                        if mouse_pressed[0] == 1:
                            self.set_pos((self.getx() + 60, self.gety() + 60))
                            self.draw()
                            music.play()
                            del star
                            return 1
            if self.crown == 1:
                if top_left == 2:
                    star.set_pos((self.getx() - 120, self.gety() - 120))
                    star.draw()
                    # Move piece when mouse click event is detected #
                    if self.getx() - 120 <= mouse_pos[0] <= self.getx() - 60 and self.gety() - 120 <= mouse_pos[1] <= self.gety() - 60:
                        if mouse_pressed[0] == 1:
                            self.set_pos((self.getx() - 120, self.gety() - 120))
                            self.draw()
                            music.play()
                            enemy.pop(enemy.index(enemy4))
                            del enemy4
                            del star
                            return 1
                if top_right == 2:
                    star.set_pos((self.getx() + 120, self.gety() - 120))
                    star.draw()
                    # Move piece when mouse click event is detected #
                    if self.getx() + 120 <= mouse_pos[0] <= self.getx() + 180 and self.gety() - 120 <= mouse_pos[1] <= self.gety() - 60:
                        if mouse_pressed[0] == 1:
                            self.set_pos((self.getx() + 120, self.gety() - 120))
                            self.draw()
                            music.play()
                            enemy.pop(enemy.index(enemy3))
                            del enemy3
                            del star
                            return 1

            if bottom_left == 2:
                star.set_pos((self.getx() - 120, self.gety() + 120))
                star.draw()
                # Move piece when mouse click event is detected #
                if self.getx() - 120 <= mouse_pos[0] <= self.getx() - 60 and self.gety() + 120 <= mouse_pos[1] <= self.gety() + 180:
                    if mouse_pressed[0] == 1:
                        self.set_pos((self.getx() - 120, self.gety() + 120))
                        self.draw()
                        music.play()
                        enemy.pop(enemy.index(enemy2))
                        del enemy2
                        del star
                        return 1
            if bottom_right == 2:
                star.set_pos((self.getx() + 120, self.gety() + 120))
                star.draw()
                # Move piece when mouse click event is detected #
                if self.getx() + 120 <= mouse_pos[0] <= self.getx() + 180 and self.gety() + 120 <= mouse_pos[1] <= self.gety() + 180:
                    if mouse_pressed[0] == 1:
                        self.set_pos((self.getx() + 120, self.gety() + 120))
                        self.draw()
                        music.play()
                        enemy.pop(enemy.index(enemy1))
                        del enemy1
                        del star
                        return 1
            if self.gety() == 420:
                self.crown = 1

    def check_crown(self, color_id):
        n = {
            0: 0,
            1: 420
        }
        if self.get_pos()[1] == n[color_id]:
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
