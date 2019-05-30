# This file is used to make the menu #
import pygame
from TextFile import *


class Menu:
    def __init__(self):
        self.screen_dim = (800, 600)
        self.display = pygame.display.set_mode(self.screen_dim)
        self.instruction = Text("Type the Server IPv4 Address:", self.display)
        self.instruction.set_pos((400 - self.instruction.get_size()[0]/2, 150))
        self.input_box_back = Background((200, 200, 200), (400, 55), (200, 160 + self.instruction.get_size()[1]), self.display)
        self.user_input = ''
        self.input_box = Chat()
        self.input_text = Text('', self.display)

    def run_menu(self):
        pygame.init()
        action = ''  # Stores the event
        run = True
        while run:
            for event in pygame.event.get():  # Returns all inputs and triggers into an array
                if event.type == pygame.QUIT:  # If the red X was clicked
                    run = False
                elif event.type == pygame.KEYDOWN:
                    action = event

            # User Interface #
            if not action == '':
                if self.input_box.edit_characters(action):
                    return self.input_box.get_text()
                action = ''
            self.input_text.set_text(self.input_box.get_text())
            self.input_text.set_size(28)
            self.input_text.set_pos((400 - (self.input_text.get_size()[0])/2, 160 + self.instruction.get_size()[1] + (55 - self.input_text.get_size()[1])/2))

            self.display.fill((255, 255, 255))

            self.instruction.draw()
            self.input_box_back.draw()
            self.input_text.draw()

            pygame.display.update()
        pygame.quit()