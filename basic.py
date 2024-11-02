import socket

port = 1337

server_socket = socket.socket()  # get instance
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('', port))  # bind host address and port together
server_socket.listen(10)
conn, address = server_socket.accept()  # accept new connection