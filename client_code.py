import socket
from cryptography.fernet import Fernet
import sys

key = b'TQenjgBHJFv6Ep4v8eN0Bayf194BS6qV_X23n5ulnRQ='

def client_program():
    host = '192.168.64.5' if len(sys.argv) == 1 else sys.argv[1] # as both code is running on same pc
    print(host)
    
    f = Fernet(key)

    port = 1337  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':

        # encrypt before sending 

        client_socket.send(f.encrypt(message.encode()))  # send message
        data = f.decrypt(str(client_socket.recv(1024).decode()))  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input
        # message will be a command

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()