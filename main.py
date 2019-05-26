'''
Title: Pygame Template
Author: John Yu
Date: 2019-04-08
'''

from Network import *
from Containers import *
from TextFile import *
from Objects import *

pygame.init()  # Loads the pygame modules in the program

# Display Variables
TITLE = 'Checkers'  # Appears in the window title
FPS = 60  # Frames per second
WIDTH = 800
HEIGHT = 600
SCREEN_DIMENSION = (WIDTH, HEIGHT)

# Color Variables
color = {
    1: (255, 255, 255),
    2: (0, 0, 0),
    3: (150, 150, 150),
    4: (255, 0, 0),
    5: (0, 255, 0),
    6: (0, 0, 255)
}

# Create the window
window = pygame.display.set_mode(SCREEN_DIMENSION)  # Creates the main surface where all other assets are placed on top
pygame.display.set_caption(TITLE)  # Updates the window title with TITLE
window.fill(color[3])  # Fills the entire surface with the color
clock = pygame.time.Clock()  # Starts a clock object to measure time


# Network #
network = Network()
player_id = network.make_connection()


# Build the Checker Board #
checkerBoard = Container()
for y in range(8):
    for x in range(8):
        if (x + y) % 2 == 0:
            checkerBoard.add(Square(window, (255, 222, 173), (x * 60, y * 60), (60, 60)))
        else:
            checkerBoard.add(Square(window, (139, 69, 19), (x * 60, y * 60), (60, 60)))

# Initial Setup for Local #
local = Player()
for y in range(3):
    for x in range(4):
        local.add(Checker(window, color[player_id], (((y % 2) * 60) + x * 120, 300 + (60 * y)), (12-(y*4+x))))

# Initial Setup for Enemy #
enemy = Player()
for y in range(3):
    for x in range(4):
        enemy.add(Checker(window, color[(player_id * 2) % 3], ((((y + 1) % 2) * 60) + x * 120, 60 * y), (y*4+x)+1))

# User Interface #
    # Backgrounds #
ui = Container()
ui.add(Background((240, 240, 240), (320, 600), (480, 0), window))  # Add the main background for the user interface
ui.add(Background((255, 255, 255), (300, 60), (490, 10), window))  # Displays turn
ui.add(Background((255, 255, 255), (300, 450), (490, 80), window))  # Chat room
ui.add(Background((255, 255, 255), (300, 50), (490, 540), window))  # Chat box
    # Text #
ui.add(Text('', window))
ui.add(Text('', window))  # Displays chat in text box

chat_box = Chat()

# --- Code Starts Here --- #
iteration = 0
run = True
turn = 1
while run:
    for event in pygame.event.get():  # Returns all inputs and triggers into an array
        if event.type == pygame.QUIT:  # If the red X was clicked
            run = False
    # Network #
    if local.get_selection() == '':  # No selection
        output = network.send_and_receive('')
    else:
        output = network.send_and_receive((local.get_selection().get_id(), (local.get_selection().getx(), local.get_selection().gety())))

    if not output == '' and output is not None:
        for item in enemy.get_list():
            if output[0] == item.get_id() and not output[1] == (420 - item.get_pos()[0], 420 - item.get_pos()[1]):
                item.pos_movement(enemy.get_list(), local.get_list(), (420 - output[1][0], 420 - output[1][1]), (1, 0, 0))
                item.draw()
                turn = (turn * 2) % 3  # Switch turns
                break

    # Checker Board #
    mousePressed = pygame.mouse.get_pressed()

    window.fill(color[3])
    checkerBoard.draw()
    local.draw()
    enemy.draw()
    if turn == player_id:
        ui.get_item(4).set_text('YOUR TURN')
        ui.get_item(4).set_pos((ui.get_item(1).get_pos()[0] + (
                (ui.get_item(1).get_size()[0] - ui.get_item(4).get_size()[0]) / 2), ui.get_item(1).get_pos()[1] + (
                                        (ui.get_item(1).get_size()[1] - ui.get_item(4).get_size()[1]) / 2)))
        if local.check_mouse_pos(pygame.mouse.get_pos(), mousePressed, enemy) == 1:
            turn = (turn * 2) % 3  # Switch turns
            local.set_test(0)
    else:
        ui.get_item(4).set_text('OPPONENT TURN')
        ui.get_item(4).set_pos((ui.get_item(1).get_pos()[0] + (
                    (ui.get_item(1).get_size()[0] - ui.get_item(4).get_size()[0]) / 2), ui.get_item(1).get_pos()[1] + (
                                            (ui.get_item(1).get_size()[1] - ui.get_item(4).get_size()[1]) / 2)))

    # User Interface #
    if iteration >= 4:
        chat_box.edit_characters(chat_box.get_key_input())
        iteration = 0
    else:
        iteration += 1
    ui.get_item(5).set_text(''.join(chat_box.get_list()))
    ui.get_item(5).set_size(20)
    ui.get_item(5).set_pos((495, 540 + (ui.get_item(3).get_size()[1] - ui.get_item(5).get_size()[1])/2))
    ui.draw()
        
    clock.tick(FPS)  # Pause the game until the FPS time is reached
    pygame.display.update()  # Updates the display
pygame.quit()