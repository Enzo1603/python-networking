from socket import socket, AF_INET, SOCK_DGRAM

server_port = 12002
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(("", server_port))
print("The server is ready to receive.")

while True:
    message, client_address = server_socket.recvfrom(2048)
    print(f"Received message: '{message.decode()}' from {client_address}")

    modified_message = message.decode().upper()
    server_socket.sendto(modified_message.encode(), client_address)
    print("Sent modified message back to client.")

server_socket.close()
