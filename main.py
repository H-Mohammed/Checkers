"""
Title: Pygame Template
Author: John Yu
Date: 2019-04-08
"""

from Network import *
from Containers import *
from Objects import *
from Menu import *
from Endscreen import *

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

music = Music()
music.set_sound('lobby_music')
music.play(-1)
connected = False
connection_failed = False
while not connected:
    # Menu #
    menu = Menu()
    ipv4 = menu.run_menu(connection_failed)

    # Network #
    try:
        network = Network(ipv4)
        player_id = network.make_connection()
        if player_id in [1, 2]:
            connected = True
        else:
            connection_failed = True

    except socket.error as e:
        connection_failed = True
music.stop()


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
chat_room = Container()
ui.add(Background((85, 67, 46), (320, 600), (480, 0), window))  # Add the main background for the user interface
ui.add(Background((239, 229, 217), (300, 60), (490, 10), window))  # Background for turn display
ui.add(Background((239, 229, 217), (300, 450), (490, 80), window))  # Chat room
ui.add(Background((239, 229, 217), (300, 50), (490, 540), window))  # Input box
    # Text #
ui.add(Text('', window))  # Displays turn
ui.add(Text('', window))  # Displays text in input box

input_box = Chat()

# --- Code Starts Here --- #
chat_to_send = ''
iteration = 0
action = ''
run = True
turn = 1
posMove = 0
while run:
    for event in pygame.event.get():  # Returns all inputs and triggers into an array
        if event.type == pygame.QUIT:  # If the red X was clicked
            run = False
        elif event.type == pygame.KEYDOWN:
            action = event
    # Network #
    if local.get_selection() == '':  # No selection
        #print('Player ' + str(player_id) + ' sent: ' + str(
            #['', '', chat_to_send]))
        output = network.send_and_receive(['', '', chat_to_send])
    else:
        #print('Player ' + str(player_id) + ' sent: ' + str(
            #[local.get_selection().get_id(), (local.get_selection().getx(), local.get_selection().gety()),
             #chat_to_send]))
        output = network.send_and_receive([local.get_selection().get_id(), (local.get_selection().getx(), local.get_selection().gety()), chat_to_send])

    chat_to_send = ''

    #print('Player ' + str(player_id) + ' received: ' + str(output))
    if not output[0] == '':
        for item in enemy.get_list():
            if output[0] == item.get_id() and not output[1] == (420 - item.get_pos()[0], 420 - item.get_pos()[1]):
                if item.pos_movement(enemy.get_list(), local.get_list(), (420 - output[1][0], 420 - output[1][1]), (1, 0, 0), 1):
                    item.draw()
                    if not item.checkCapture(local.get_list(), enemy.get_list()):
                        turn = (turn * 2) % 3  # Switch turns
                    break
                break
    # Check if enemy piece is crowned #
    for item in enemy.get_list():
        item.check_crown(1)

    # Checker Board #
    mousePressed = pygame.mouse.get_pressed()

    for x in local.get_list():
        x.check_crown(0)

    window.fill(color[3])
    checkerBoard.draw()
    local.draw()
    enemy.draw()
    if turn == player_id:
        ui.get_item(4).set_text('YOUR TURN')
        ui.get_item(1).set_color((0, 255, 0))
        ui.get_item(4).set_pos((ui.get_item(1).get_pos()[0] + (
                (ui.get_item(1).get_size()[0] - ui.get_item(4).get_size()[0]) / 2), ui.get_item(1).get_pos()[1] + (
                                        (ui.get_item(1).get_size()[1] - ui.get_item(4).get_size()[1]) / 2)))
        temp = local.check_mouse_pos(pygame.mouse.get_pos(), mousePressed, enemy, 0)
        if temp[0] == 2:
            while temp[1].checkCapture(enemy.get_list(), local.get_list()):
                if temp[1].pos_movement(enemy.get_list(), local.get_list(), pygame.mouse.get_pos(), pygame.mouse.get_pressed(), 0) == 2:
                    pass
                else:
                    break
            turn = (turn * 2) % 3  # Switch turns
            local.set_test(0)
        elif temp[0] == 1:
            turn = (turn * 2) % 3  # Switch turns
            local.set_test(0)

    else:
        ui.get_item(4).set_text('OPPONENT TURN')
        ui.get_item(1).set_color((255, 0, 0))
        ui.get_item(4).set_pos((ui.get_item(1).get_pos()[0] + (
                    (ui.get_item(1).get_size()[0] - ui.get_item(4).get_size()[0]) / 2), ui.get_item(1).get_pos()[1] + (
                                            (ui.get_item(1).get_size()[1] - ui.get_item(4).get_size()[1]) / 2)))

    # User Interface #
    if not action == '':
        if input_box.edit_characters(action):
            chat_to_send = input_box.get_text()
            chat_room.offset_all((0, -20))
            chat_room.add(Text(input_box.get_text(), window, (500, 500), (0, 0, 0), 20))
            input_box.reset_characters()
        action = ''
    else:
        chat_to_send = ''

    if len(output[2]) > 0:
        chat_room.offset_all((0, -20))
        chat_room.add(Text(output[2][0], window, (500, 500), (0, 0, 0), 20))

    for index, word in enumerate(chat_room.get_list()):
        if word.get_pos()[1] <= 80:
            chat_room.get_list().pop(index)
            del word

    ui.get_item(5).set_text(input_box.get_text())
    ui.get_item(5).set_size(20)
    ui.get_item(5).set_pos((495, 540 + (ui.get_item(3).get_size()[1] - ui.get_item(5).get_size()[1]) / 2))
    ui.draw()
    chat_room.draw()

    # Win/Lose Algorithm #
    if len(local.get_list()) == 0:  # You lose
        output = network.send_and_receive(
            [local.get_selection().get_id(), (local.get_selection().getx(), local.get_selection().gety()),
             chat_to_send])
        endscreen = Endscreen('boo')
        endscreen.run_endscreen()
    if len(enemy.get_list()) == 0:  # You win
        output = network.send_and_receive(
            [local.get_selection().get_id(), (local.get_selection().getx(), local.get_selection().gety()),
             chat_to_send])
        endscreen = Endscreen('applause')
        endscreen.run_endscreen()

    posMove = 1
    for i in local.get_list():
        if i.checkMovement(local.get_list(), enemy.get_list(), 0):
            posMove = 0
    
    if posMove == 1:
        for i in enemy.get_list():
            if i.checkMovement(enemy.get_list(), local.get_list(), 1):
                output = network.send_and_receive(
                    [local.get_selection().get_id(), (local.get_selection().getx(), local.get_selection().gety()),
                     chat_to_send])
                endscreen = Endscreen('applause')
                endscreen.run_endscreen()
                break
        print('Tie')

    clock.tick(FPS)  # Pause the game until the FPS time is reached
    pygame.display.update()  # Updates the display
pygame.quit()