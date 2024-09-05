from socket import socket, AF_INET, SOCK_DGRAM


server_name = "192.168.178.15"
server_port = 80

# AF_INET is the address family for IPv4
# SOCK_DGRAM is the socket type for UDP
client_socket = socket(AF_INET, SOCK_DGRAM)

message = input("Input lowercase sentence: ")

client_socket.sendto(message.encode(), (server_name, server_port))

modified_message, server_address = client_socket.recvfrom(2048)
print(modified_message.decode())

client_socket.close()
