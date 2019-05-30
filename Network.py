import socket, pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = '192.168.1.69'
        self.port = 5555
        self.addr = (self.server, self.port)

    # Method tries to connect with server and return information sent by the server #
    def make_connection(self):
        try:
            self.client.connect(self.addr)  # Connect the client to the server
            return pickle.loads(self.client.recv(2048))  # Return the initial info of pieces
        except socket.error as e:
            print(e)

    # Method sends input and receives output #
    def send_and_receive(self, data):
        try:
            self.client.send(pickle.dumps(data))  # Sends friendly piece information to the server
            return pickle.loads(self.client.recv(2048))  # Returns enemy piece information from the server
        except socket.error as e:
            print(e)