# This file contains objects that aggregate other objects #


# Class creates container objects
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

    def offset_all(self, offset):
        for item in self.list:
            item.set_pos((item.get_pos()[0] + offset[0], item.get_pos()[1] + offset[1]))



# Class creates player objects
class Player(Container):  # Stores pieces
    def __init__(self):
        super().__init__()
        self.selection = ''  # Stores the selected piece
        self.test = 0

    def check_mouse_pos(self, mouse_pos, mouse_pressed, enemy, color):
        for item in self.list:
            if item.getx() <= mouse_pos[0] <= item.getx() + item.get_width() and item.gety() <= mouse_pos[1] <= item.gety() + item.get_height():
                if mouse_pressed[0] == 1:
                    self.selection = item
                    self.test = 1
                    return (item.pos_movement(self.list, enemy.get_list(), mouse_pos, mouse_pressed, color), self.selection)

        if self.test == 1:
            return (self.selection.pos_movement(self.list, enemy.get_list(), mouse_pos, mouse_pressed, color), self.selection)
        return (0, 0)

    def get_selection(self):
        return self.selection

    def set_selection(self, var):
        self.selection = var

    def set_test(self, num):
        self.test = num
