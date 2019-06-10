from _thread import *
import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind(('', 5555))
except socket.error as e:
    print(e)

s.listen(2)

selection = [['', '', [], 0], ['', '', [], 0]]  # Stores the selected piece information of each client


# functions #
def threaded_client(conn, player):
    conn.send(pickle.dumps(player))  # Sends the player id to the client
    while True:
        try:
            new_data = pickle.loads(conn.recv(2048))  # Get new positions made by the client
            print('player ' + str((player % 2) + 1) + ' received: ' + str(new_data))
            # Update Selection of Current Player #
            selection[player - 1][0] = new_data[0]
            selection[player - 1][1] = new_data[1]
            if not new_data[2] == '':
                selection[player - 1][2].append(new_data[2])  # Queues text/emoji to be sent
            # Send enemy info to client #
            selection[player - 1][3] = new_data[3]
            print('player ' + str((player % 2) + 1) + ' sent: ' + str(selection[player % 2]))
            conn.sendall(pickle.dumps(selection[player % 2]))
            if selection[(player % 2)][3] in [1, 2]:
                selection[(player % 2)][3] = 0
            if len(selection[player % 2][2]) > 0:
                selection[player % 2][2].pop(0)
        except Exception as n:
            print(n)
            break

    print('Connection Lost ... ')
    conn.close()


# Thread Starts Here #
current_player = 1
while True:
    c, address = s.accept()  # Accepts connection from client
    print('Connected to:', address)

    start_new_thread(threaded_client, (c, current_player))
    current_player += 1
