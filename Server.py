from _thread import *
import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind(('', 5555))
except socket.error as e:
    print(e)

s.listen(2)


# functions #
def threaded_client(conn, player):
    conn.send(pickle.dumps(player))  # Sends the player id to the client
    while True:
        try:
            new_data = pickle.loads(conn.recv(2048))  # Get new positions made by the client
            if not new_data:
                print('Disconnected...')
                break
            else:
                if player == 1:
                    reply = pickle.dumps('This is John')  # Return Black Data
                else:
                    reply = pickle.dumps('This is Pi')

            conn.sendall(reply)  # Send reply to clients
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
