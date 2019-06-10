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

temporary_button = Background((0, 0, 0), (50, 50), (5, 545), window)
emoji_button_cool = Button(window, (125, 485), (50, 50), 'media/cool.png')
emoji_button_dying_of_laughter = Button(window, (125, 545), (50, 50), 'media/dying_of_laughter.png')
emoji_button_laugh = Button(window, (185, 485), (50, 50), 'media/laugh.png')
emoji_button_nerd = Button(window, (185, 545), (50, 50), 'media/nerd.png')
emoji_button_neutral = Button(window, (245, 485), (50, 50), 'media/neutral.png')
emoji_button_sad = Button(window, (245, 545), (50, 50), 'media/sad.png')
emoji_button_smile = Button(window, (305, 485), (50, 50), 'media/smile.png')
emoji_button_sneaky = Button(window, (305, 545), (50, 50), 'media/sneaky.png')
emoji_button_surprise = Button(window, (365, 485), (50, 50), 'media/surprise.png')
emoji_button_whistle = Button(window, (365, 545), (50, 50), 'media/whistle.png')
emoji_button_wink = Button(window, (425, 485), (50, 50), 'media/wink.png')
emoji_button_wrath = Button(window, (425, 545), (50, 50), 'media/wrath.png')

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

    #print('Player ' + str(player_id) + ' received: ' + str(output))
    if not output[0] == '':
        for item in enemy.get_list():
            if output[0] == item.get_id() and not output[1] == (420 - item.get_pos()[0], 420 - item.get_pos()[1]):
                move = item.pos_movement(enemy.get_list(), local.get_list(), (420 - output[1][0], 420 - output[1][1]), (1, 0, 0), 1)
                if move[0] in [1, 2]:
                    item.draw()
                    undo.append([[x.get_pos() for x in local.get_list()], [x.get_pos() for x in enemy.get_list()]])
                    temparray.append(0)
                    if move[0] == 2:
                        undo[-1][1].append(move[1])
                        temparray[-1]=2
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
    if 5 <= pygame.mouse.get_pos()[0] <= 55 and 545 <= pygame.mouse.get_pos()[1] <= 595 and iteration2 == 0:
        if pygame.mouse.get_pressed()[0]:
            if turn == player_id:
                player_hit_undo = 1
    if output[3] in [1, 2]:
        if (5 <= pygame.mouse.get_pos()[0] <= 55 and 545 <= pygame.mouse.get_pos()[1] <= 595 and iteration2 == 0) or output[3] == 2:
            if (pygame.mouse.get_pressed()[0]) or output[3] == 2:
                if len(undo) > 1:
                    if temparray[-2] == 1:  # Yes or no value that specifies if piece got removed in enemy or local
                        for i in range(len(local.get_list())):
                            if local.get_list()[i].get_id() < undo[-2][0][-1].getid():
                                local.get_list().insert(i, undo[-2][0].pop(-1))
                    if temparray[-2] == 2:
                        for i in range(len(enemy.get_list())):
                            if enemy.get_list()[i].get_id() < undo[-2][1][-1].getid():
                                enemy.get_list().insert(i, undo[-2][1].pop(-1))
                    for i in range(len(local.get_list())):
                        print("This undo: " + str(undo))
                        local.get_list()[i].set_pos(undo[-2][0][i])
                    for i in range(len(enemy.get_list())):
                        enemy.get_list()[i].set_pos(undo[-2][1][i])
                    undo.pop(len(undo) - 2)
                    temparray.pop(-2)
                    iteration2 += 1
                    player_hit_undo = 2


    if turn == player_id:
        ui.get_item(4).set_text('YOUR TURN')
        ui.get_item(1).set_color((0, 255, 0))
        ui.get_item(4).set_pos((ui.get_item(1).get_pos()[0] + (
                (ui.get_item(1).get_size()[0] - ui.get_item(4).get_size()[0]) / 2), ui.get_item(1).get_pos()[1] + (
                                        (ui.get_item(1).get_size()[1] - ui.get_item(4).get_size()[1]) / 2)))
        temp = local.check_mouse_pos(pygame.mouse.get_pos(), mousePressed, enemy, 0)
        if temp[0][0] == 1 or temp[0][0] == 2:
            undo.append([[x.get_pos() for x in local.get_list()], [x.get_pos() for x in enemy.get_list()]])
            temparray.append(0)
            iteration2 = 0
        if temp[0][0] == 2:
            undo[-1][1].append(temp[0][1])
            temparray[-1] += 1
            while temp[1].checkCapture(enemy.get_list(), local.get_list()):
                if temp[1].pos_movement(enemy.get_list(), local.get_list(), pygame.mouse.get_pos(), pygame.mouse.get_pressed(), 0) == 2:
                    undo.append([[x.get_pos() for x in local.get_list()], [x.get_pos() for x in enemy.get_list()]])
                    undo[-1][1].append(temp[0][1])
                    temparray.append(1)
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
        endscreen = Endscreen('boo', "You Suck")
        endscreen.run_endscreen()
    if len(enemy.get_list()) == 0:  # You win
        output = network.send_and_receive(
            [local.get_selection().get_id(), (local.get_selection().getx(), local.get_selection().gety()),
             chat_to_send])
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

    temporary_button.draw()
    emoji_button_cool.draw()
    emoji_button_dying_of_laughter.draw()
    emoji_button_laugh.draw()
    emoji_button_nerd.draw()
    emoji_button_neutral.draw()
    emoji_button_sad.draw()
    emoji_button_smile.draw()
    emoji_button_sneaky.draw()
    emoji_button_surprise.draw()
    emoji_button_whistle.draw()
    emoji_button_wink.draw()
    emoji_button_wrath.draw()

    clock.tick(FPS)  # Pause the game until the FPS time is reached
    pygame.display.update()  # Updates the display
pygame.quit()