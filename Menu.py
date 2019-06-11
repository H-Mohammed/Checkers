# This file is used to make the menu #
from TextFile import *
from Mixer import *


class Menu:
    def __init__(self):
        self.screen_dim = (800, 600)
        self.display = pygame.display.set_mode(self.screen_dim)
        self.instruction = Text("Enter the Server IPv4 Address:", self.display)
        self.instruction.set_pos((400 - self.instruction.get_size()[0]/2, 150))
        self.input_box_back = Background((200, 200, 200), (400, 55), (200, 160 + self.instruction.get_size()[1]), self.display)
        self.user_input = ''
        self.input_box = Chat()
        self.input_text = Text('', self.display)
        self.connection_failed_text = Text('', self.display)
        self.background = ''
        self.music = Music()
        self.music.set_sound('lobby_music')
        self.clock = pygame.time.Clock()

    def run_menu(self, connection_failed):
        pygame.init()
        action = ''  # Stores the event
        img = 1
        self.music.play(0)
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
                    self.music.stop()
                    return self.input_box.get_text()
                action = ''
            self.input_text.set_text(self.input_box.get_text())
            self.input_text.set_size(28)
            self.input_text.set_pos((400 - (self.input_text.get_size()[0])/2, 160 + self.instruction.get_size()[1] + (55 - self.input_text.get_size()[1])/2))

            if 1 <= img <= 9:
                unicode = '0000' + str(img)
            elif 10 <= img <= 99:
                unicode = '000' + str(img)
            elif 100 <= img <= 999:
                unicode = '00' + str(img)
            elif 1000 <= img <= 9999:
                unicode = '0' + str(img)
            self.display.blit(pygame.image.load('lobby_playback/scene' + unicode + '.png'), (0, 0))
            img += 1
            if img > 2552:
                img = 1
                self.music.stop()
                self.music.play()

            self.instruction.draw()
            self.input_box_back.draw()
            self.input_text.draw()

            if connection_failed:
                self.connection_failed_text.set_text("Connection Failed. Try Again.")
                self.connection_failed_text.set_color((255, 0, 0))
                self.connection_failed_text.set_size(24)
                self.connection_failed_text.set_pos((400 - (self.connection_failed_text.get_size()[0]/2), 270))
                self.connection_failed_text.draw()
            self.clock.tick(28)
            pygame.display.update()
        pygame.quit()