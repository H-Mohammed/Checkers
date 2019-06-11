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
from Button import *

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

enemy_pieces = []
local_pieces = []
for i in range(len(enemy.get_list())):
    enemy_pieces.append(enemy.get_list()[i])
for i in range(len(local.get_list())):
    local_pieces.append(local.get_list()[i])
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

emoji_background = Background((239, 229, 217), (480, 120), (0, 480), window)
emoji_button = [Button(window, (125, 485), (50, 50), 1, 'media/cool.png'),
         Button(window, (125, 545), (50, 50), 2, 'media/dying_of_laughter.png'),
         Button(window, (185, 485), (50, 50), 3, 'media/laugh.png'),
         Button(window, (185, 545), (50, 50), 4, 'media/nerd.png'),
         Button(window, (245, 485), (50, 50), 5, 'media/neutral.png'),
         Button(window, (245, 545), (50, 50), 6, 'media/sad.png'),
         Button(window, (305, 485), (50, 50), 7, 'media/smile.png'),
         Button(window, (305, 545), (50, 50), 8, 'media/sneaky.png'),
         Button(window, (365, 485), (50, 50), 9, 'media/surprise.png'),
         Button(window, (365, 545), (50, 50), 10, 'media/whistle.png'),
         Button(window, (425, 485), (50, 50), 11, 'media/wink.png'),
         Button(window, (425, 545), (50, 50), 12, 'media/wrath.png')]

input_box = Chat()

# --- Code Starts Here --- #
chat_to_send = ''
iteration = 0
action = ''
run = True
turn = 1
posMove = 0
undo = []
iteration2 = 0
temp_local_list = []
temparray = [0]
player_hit_undo = 0
mouse_down = False
for i in local.get_list():
    temp_local_list.append(i)
temp_enemy_list = []
for j in enemy.get_list():
    temp_enemy_list.append(j)
undo.append([temp_local_list, temp_enemy_list])
while run:
    for event in pygame.event.get():  # Returns all inputs and triggers into an array
        if event.type == pygame.QUIT:  # If the red X was clicked
            run = False
        elif event.type == pygame.KEYDOWN:
            action = event
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True
    # Network #
    if local.get_selection() == '':  # No selection
        #print('Player ' + str(player_id) + ' sent: ' + str(
            #['', '', chat_to_send]))
        output = network.send_and_receive(['', '', chat_to_send, player_hit_undo])
    else:
        #print('Player ' + str(player_id) + ' sent: ' + str(
            #[local.get_selection().get_id(), (local.get_selection().getx(), local.get_selection().gety()),
             #chat_to_send]))
        output = network.send_and_receive([local.get_selection().get_id(), (local.get_selection().getx(), local.get_selection().gety()), chat_to_send, player_hit_undo])

    chat_to_send = ''
    if player_hit_undo >= 2:
        player_hit_undo = output[3]

    #print('Player ' + str(player_id) + ' received: ' + str(output))
    if not output[0] == '':
        for item in enemy.get_list():
            if output[0] == item.get_id() and not output[1] == (420 - item.get_pos()[0], 420 - item.get_pos()[1]):
                move = item.pos_movement(enemy.get_list(), local.get_list(), (420 - output[1][0], 420 - output[1][1]), (1, 0, 0), 1)
                if move[0] in [1, 2]:
                    item.draw()
                    undo.append([[x.get_pos() for x in local_pieces], [x.get_pos() for x in enemy_pieces]])
                    temparray.append(0)
                    if move[0] == 2:
                        undo[-1][0].append(move[1])
                        temparray[-1] = 1
                    #print(move)
                    if item.check_capture_flipped(local.get_list(), enemy.get_list()) and move[0] == 2:
                        pass
                    else:
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
    enemy.draw()

    if turn == player_id:
        ui.get_item(4).set_text('YOUR TURN')
        ui.get_item(1).set_color((0, 255, 0))
        ui.get_item(4).set_pos((ui.get_item(1).get_pos()[0] + (
                (ui.get_item(1).get_size()[0] - ui.get_item(4).get_size()[0]) / 2), ui.get_item(1).get_pos()[1] + (
                                        (ui.get_item(1).get_size()[1] - ui.get_item(4).get_size()[1]) / 2)))
        temp = local.check_mouse_pos(pygame.mouse.get_pos(), mousePressed, enemy, 0)
        if temp[0][0] == 1 or temp[0][0] == 2:
            undo.append([[x.get_pos() for x in local_pieces], [x.get_pos() for x in enemy_pieces]])
            temparray.append(0)

        if temp[0][0] == 2:
            undo[-1][1].append(temp[0][1])
            temparray[-1] = 2
            while temp[1].checkCapture(enemy.get_list(), local.get_list()):
                if temp[1].pos_movement(enemy.get_list(), local.get_list(), pygame.mouse.get_pos(), pygame.mouse.get_pressed(), 0) == 2:
                    undo.append([[x.get_pos() for x in local_pieces], [x.get_pos() for x in enemy_pieces]])
                    undo[-1][1].append(temp[0][1])
                    temparray.append(2)
                else:
                    break
            turn = (turn * 2) % 3  # Switch turns
            local.set_test(0)
        elif temp[0][0] == 1:
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

    if mouse_down:
        for x in emoji_button:
            if x.get_click():
                chat_to_send = x.get_id()
                chat_room.offset_all((0, -60))
                image = {
                    1: 'media/cool.png',
                    2: 'media/dying_of_laughter.png',
                    3: 'media/laugh.png',
                    4: 'media/nerd.png',
                    5: 'media/neutral.png',
                    6: 'media/sad.png',
                    7: 'media/smile.png',
                    8: 'media/sneaky.png',
                    9: 'media/surprise.png',
                    10: 'media/whistle.png',
                    11: 'media/wink.png',
                    12: 'media/wrath.png'
                }
                chat_room.add(Emoji(image[x.get_id()], (0, 0, 0), (500, 470), window))
    mouse_down = False

    if len(output[2]) > 0:
        print(type(output[2][0]).__name__)
        if type(output[2][0]).__name__ == 'str':
            chat_room.offset_all((0, -20))
            chat_room.add(Text(output[2][0], window, (500, 500), (0, 0, 0), 20))
        elif type(output[2][0]).__name__ == 'int':
            image = {
                1: 'media/cool.png',
                2: 'media/dying_of_laughter.png',
                3: 'media/laugh.png',
                4: 'media/nerd.png',
                5: 'media/neutral.png',
                6: 'media/sad.png',
                7: 'media/smile.png',
                8: 'media/sneaky.png',
                9: 'media/surprise.png',
                10: 'media/whistle.png',
                11: 'media/wink.png',
                12: 'media/wrath.png'
            }
            chat_room.offset_all((0, -60))
            chat_room.add(Emoji(image[output[2][0]], (0, 0, 0), (500, 470), window))

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
             chat_to_send, 0])
        endscreen = Endscreen('boo', "You Lose")
        endscreen.run_endscreen()
    if len(enemy.get_list()) == 0:  # You win
        output = network.send_and_receive(
            [local.get_selection().get_id(), (local.get_selection().getx(), local.get_selection().gety()),
             chat_to_send, 0])
        endscreen = Endscreen('applause', "You Win")
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
                endscreen = Endscreen('applause', "You Win")
                endscreen.run_endscreen()
                break
        print('Tie')
    emoji_background.draw()

    for x in emoji_button:
        x.draw()

    clock.tick(FPS)  # Pause the game until the FPS time is reached
    pygame.display.update()  # Updates the display
pygame.quit()