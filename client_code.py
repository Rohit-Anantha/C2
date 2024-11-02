import socket
from cryptography.fernet import Fernet
import sys
import time

key = b'TQenjgBHJFv6Ep4v8eN0Bayf194BS6qV_X23n5ulnRQ='

def client_program():
    host = '192.168.64.5' if len(sys.argv) == 1 else sys.argv[1] 
    print(host)
    
    f = Fernet(key)

    port = 1337  # socket server port number

    counter = 0
    while True:
        try:
            # Try to connect and break out of our spin loop
            client_socket = socket.socket()  # instantiate
            client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            client_socket.connect((host, port))  # connect to the server
            
            break
        except socket.error:
            # retry our connection if it doesn't work
            sleep_time = 7
            print("Connection Failed, Retrying in ", sleep_time, "...")
            counter += sleep_time
            time.sleep(sleep_time)

    print('Connected after:', counter // 60 ,'minutes, ', counter % 60, 'seconds.') 
    
    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':

        # encrypt before sending 

        client_socket.send(f.encrypt(bytes(message.encode())))  # send message
        data = f.decrypt(client_socket.recv(65536)) # receive response

        print('Received from server: \n' + data.decode())  # show in terminal

        message = input(" -> ")  # again take input
        # message will be a command

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()