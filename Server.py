from _thread import *
import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind(('', 5555))
except socket.error as e:
    print(e)

s.listen(2)

selection = [['', '', []], ['', '', []]]  # Stores the selected piece information of each client


# functions #
def threaded_client(conn, player):
    conn.send(pickle.dumps(player))  # Sends the player id to the client
    while True:
        try:
            new_data = pickle.loads(conn.recv(2048))  # Get new positions made by the client
            # Update Selection of Current Player #
            selection[player - 1][0] = new_data[0]
            selection[player - 1][1] = new_data[1]
            if not new_data[2] == '':
                selection[player - 1][2].append(new_data[2])
            # Send enemy info to client #
            conn.sendall(pickle.dumps(selection[player % 2]))
            if not selection[player % 2][2] == []:
                selection[player % 2][2].pop(0)
        except socket.error:
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
