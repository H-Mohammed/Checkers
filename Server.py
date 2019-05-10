from _thread import *
from Network import *

n = Network()
server = n.getServer()  # Set server to local IPv4 Address
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((server, port))
except socket.error as e:
    print(e)

s.listen(2)

# Starter Info #


# functions #
def ThreatedClient(conn, player):
    conn.send(pickle.dumps(info[player]))  # Send the starting positions of pieces to client
    while True:
        try:
            new_data = pickle.loads(conn.recv(2048))  # Get new positions made by the client
            info[player] = new_data
            if not new_data:
                print('Disconnected...')
                break
            else:
                if player == 0:
                    reply = pickle.dumps(info[1])  # Return Black Data
                else:
                    reply = pickle.dumps(info[0])

            conn.sendall(reply)  # Send reply to clients
        except:
            break

    print('Connection Lost ... ')
    conn.close()

# Thread Starts Here #
current_player = 0
while True:
    c, address = s.accept()  # Accepts connection from client
    print('Connected to:', address)

    start_new_thread(ThreatedClient, (c, current_player))
    current_player += 1