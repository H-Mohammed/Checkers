import pygame


# This is used to create text and emoji objects #
class Parent:
    def __init__(self, color, pos, window):
        self.color = color
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.window = window

    def get_pos(self):
        return self.pos

    def set_pos(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.pos = pos


class Emoji(Parent):
    def __init__(self, img, color, pos, window):
        super().__init__(color, pos, window)
        self.img = pygame.image.load(img)

    def draw(self):
        self.window.blit(self.img, self.pos)


# Method creates text objects #
class Text(Parent):
    def __init__(self, text, window, pos=(0, 0), color=(0, 0, 0), size=28):
        super().__init__(color, pos, window)
        self.size = size
        self.text = text
        self.font_family = 'Times New Roman'
        self.font = pygame.font.SysFont(self.font_family, self.size)
        self.surface = self.font.render(self.text, 1, self.color)

    def draw(self):
        self.window.blit(self.surface, self.pos)

    def get_text(self):
        return self.surface

    def get_size(self):
        return self.font.size(self.text)

    def move_text(self, size):
        pass

    def set_color(self, color):
        self.color = color
        self.surface = self.font.render(self.text, 1, self.color)

    def set_size(self, size):
        self.size = size
        self.font = pygame.font.SysFont(self.font_family, self.size)
        self.surface = self.font.render(self.text, 1, self.color)

    def set_text(self, text):
        self.text = text
        self.font = pygame.font.SysFont(self.font_family, self.size)
        self.surface = self.font.render(self.text, 1, self.color)


# Method creates background for text objects #
class Background(Parent):
    def __init__(self, color, size, pos, surface):
        super().__init__(color, pos, surface)
        self.size = size
        self.width = size[0]
        self.height = size[1]
        self.rect = (self.x, self.y, self.width, self.height)

    def draw(self):
        pygame.draw.rect(self.window, self.color, self.rect)

    def get_size(self):
        return self.size

    def set_color(self, color):
        self.color = color


# Class creates chat box #
class Chat:
    def __init__(self):
        self.keys = pygame.key.get_pressed()
        self.user_input = ''

    def edit_characters(self, event):
        if event.key == pygame.K_BACKSPACE:
            self.user_input = self.user_input[:-1]
            return False
        elif event.key == pygame.K_RETURN:
            if self.user_input == '':
                return False
            else:
                return True
        else:
            self.user_input += event.unicode
            return False

    def reset_characters(self):
        self.user_input = ''

    def get_text(self):
        return self.user_input
