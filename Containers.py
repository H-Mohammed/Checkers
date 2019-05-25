# This file contains objects that aggregate other objects #


class Container:  # Parent class for all objects that aggregate other objects
    def __init__(self):
        self.list = []

    def add(self, obj):
        self.list.append(obj)

    def draw(self):
        for item in self.list:
            item.draw()
    
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
