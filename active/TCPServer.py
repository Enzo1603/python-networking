from socket import socket, AF_INET, SOCK_STREAM

server_port = 7001

# AF_INET is the address family for IPv4
# SOCK_STREAM is the socket type for TCP
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(("", server_port))

server_socket.listen(1)
print(f"The server is ready to receive on port {server_port}.")

while True:
    connection_socket, client_address = server_socket.accept()
    message = connection_socket.recv(1024).decode()
    print(f"Received message: '{message}' from {client_address}")

    modified_message = message.upper()

    connection_socket.send(modified_message.encode())
    print("Sent modified message back to client.")
    connection_socket.close()

server_socket.close()
