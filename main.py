'''
Title: Pygame Template
Author: John Yu
Date: 2019-04-08
'''

from Network import *
from Containers import *
from TextFile import *

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
player = network.make_connection()
print(player)
data = network.send_and_receive('Hello World')
print(data)


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
        local.add(Checker(window, color[player], (((y % 2) * 60) + x * 120, 300 + (60 * y))))

# Initial Setup for Enemy #
enemy = Player()
for y in range(3):
    for x in range(4):
        enemy.add(Checker(window, color[(player * 2) % 3], ((((y + 1) % 2) * 60) + x * 120, 60 * y)))

# --- Code Starts Here --- #
run = True
turn = 1
while run:
    for event in pygame.event.get():  # Returns all inputs and triggers into an array
        if event.type == pygame.QUIT:  # If the red X was clicked
            run = False
    mousePressed = pygame.mouse.get_pressed()

    checkerBoard.draw()
    local.draw()
    enemy.draw()
    if turn == player:
        if local.check_mouse_pos(pygame.mouse.get_pos(), mousePressed, enemy) == 1:
            turn = (turn * 2) % 3  # Switch turns
            local.set_selection('')
            local.set_test(0)
        
    clock.tick(FPS)  # Pause the game until the FPS time is reached
    pygame.display.update()  # Updates the display
pygame.quit()