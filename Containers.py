# This file contains objects that aggregate other objects #
import pygame


class Container:  # Parent class for all objects that aggregate other objects
    def __init__(self):
        self.list = []

    def add(self, obj):
        self.list.append(obj)

    def draw(self):
        for item in self.list:
            item.draw()

    def get_item(self, index):
        return self.list[index]
    
    def get_list(self):
        return self.list


class Player(Container):  # Stores pieces
    def __init__(self):
        super().__init__()
        self.selection = ''  # Stores the selected piece
        self.test = 0

    def check_mouse_pos(self, mouse_pos, mouse_pressed, enemy):
        for item in self.list:
            if item.getx() <= mouse_pos[0] <= item.getx() + item.get_width() and item.gety() <= mouse_pos[1] <= item.gety() + item.get_height():
                if mouse_pressed[0] == 1:
                    self.selection = item
                    self.test = 1
                    return item.pos_movement(self.list, enemy.get_list(), mouse_pos, mouse_pressed)

        if self.test == 1:
            return self.selection.pos_movement(self.list, enemy.get_list(), mouse_pos, mouse_pressed)

    def get_selection(self):
        return self.selection

    def set_selection(self, var):
        self.selection = var

    def set_test(self,num):
        self.test = num


class Chat(Container):
    def __init__(self):
        super().__init__()
        self.keys = pygame.key.get_pressed()

    def get_key_input(self):
        print(pygame.K_LSHIFT)
        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_BACKSPACE]:
            return pygame.K_BACKSPACE
        elif self.keys[pygame.K_SPACE]:
            return pygame.K_SPACE
        elif self.keys[pygame.K_KP_ENTER]:
            return pygame.K_KP_ENTER
        else:
            for x in range(pygame.K_a, pygame.K_z + 1):
                if self.keys[x]:
                    if self.keys[pygame.K_LSHIFT] or self.keys[pygame.K_RSHIFT] or self.keys[pygame.K_CAPSLOCK]:
                        return x + 1000
                    else:
                        return x
        return False

    def edit_characters(self, key):
        if key is False:
            return
        if key == pygame.K_BACKSPACE:
            if len(self.list) > 0:
                self.list.pop()
        elif key == pygame.K_SPACE:
            self.list.append(' ')
        elif key == pygame.K_KP_ENTER:
            # Submit characters
            pass
        else:
            letters = {
                97: 'a',
                98: 'b',
                99: 'c',
                100: 'd',
                101: 'e',
                102: 'f',
                103: 'g',
                104: 'h',
                105: 'i',
                106: 'j',
                107: 'k',
                108: 'l',
                109: 'm',
                110: 'n',
                111: 'o',
                112: 'p',
                113: 'q',
                114: 'r',
                115: 's',
                116: 't',
                117: 'u',
                118: 'v',
                119: 'w',
                120: 'x',
                121: 'y',
                122: 'z',
                1097: 'A',
                1098: 'B',
                1099: 'C',
                1100: 'D',
                1101: 'E',
                1102: 'F',
                1103: 'G',
                1104: 'H',
                1105: 'I',
                1106: 'J',
                1107: 'K',
                1108: 'L',
                1109: 'M',
                1110: 'N',
                1111: 'O',
                1112: 'P',
                1113: 'Q',
                1114: 'R',
                1115: 'S',
                1116: 'T',
                1117: 'U',
                1118: 'V',
                1119: 'W',
                1120: 'X',
                1121: 'Y',
                1122: 'Z',

            }
            self.list.append(letters[key])