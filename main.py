'''
Title: Pygame Template
Author: John Yu
Date: 2019-04-08
'''

import pygame
from Network import *

pygame.init()  # Loads the pygame modules in the program

# Display Variables
TITLE = 'Hello World'  # Appears in the window title
FPS = 60  # Frames per second
WIDTH = 800
HEIGHT = 600
SCREEN_DIMENSION = (WIDTH, HEIGHT)

# Color Variables
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (150, 150, 150)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Create the window
window = pygame.display.set_mode(SCREEN_DIMENSION)  # Creates the main surface where all other assets are placed on top
pygame.display.set_caption(TITLE)  # Updates the window title with TITLE
window.fill(GREY)  # Fills the entire surface with the color
clock = pygame.time.Clock()  # Starts a clock object to measure time

# Network #
network = Network()
local_client_information = network.Make_Connection()

# --- Code Starts Here --- #
run = True

while run:
    for event in pygame.event.get():  # Returns all inputs and triggers into an array
        if event.type == pygame.QUIT:  # If the red X was clicked
            run = False
    clock.tick(FPS)  # Pause the game until the FPS time is reached
    pygame.display.update()  # Updates the display
pygame.quit()