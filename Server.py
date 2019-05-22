from _thread import *
from Network import *

n = Network()
server = n.getServer()
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind(('', port))
except socket.error as e:
    print(e)
s.listen(2)

# Starter Info #


# functions #
def ThreatedClient(conn, player):
    #conn.send(pickle.dumps(info[player]))  # Send the starting positions of pieces to client
    conn.send(pickle.dumps('Connection Established'))
    while True:
        try:
            new_data = pickle.loads(conn.recv(2048))  # Get new positions made by the client
            print(new_data)
            #info[player] = new_data
            if not new_data:
                print('Disconnected...')
                break
            else:
                if player == 0:
                    reply = pickle.dumps('This is John')  # Return Black Data
                else:
                    reply = pickle.dumps('This is Pi')

            conn.sendall(pickle.dumps(reply))  # Send reply to clients
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