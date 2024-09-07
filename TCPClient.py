from socket import socket, AF_INET, SOCK_STREAM

# server_name = "192.168.178.151"
# server_port = 12002
server_name = "127.0.0.1"
server_port = 5001

# AF_INET is the address family for IPv4
# SOCK_STREAM is the socket type for TCP
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name, server_port))

message = input("Input lowercase sentence: ")

client_socket.send(message.encode())

modified_message = client_socket.recv(1024)
print(modified_message.decode())

client_socket.close()
