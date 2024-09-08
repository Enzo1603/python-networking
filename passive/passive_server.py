import socket
import threading

TCP_PORT = 7001
UDP_PORT = 7002


def start_tcp_server():
    # Erstelle einen TCP/IP-Socket (AF_INET: IPv4, SOCK_STREAM: TCP)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Binde den Socket an die Adresse (localhost) und Port (TCP_PORT)
    server_address = ("localhost", TCP_PORT)
    server_socket.bind(server_address)

    # Warte auf eingehende Verbindungen
    server_socket.listen(1)
    print(f"TCP-Server wartet auf eingehenden Traffic auf Port {TCP_PORT}...")

    while True:
        # Warte auf eine Verbindung
        connection, client_address = server_socket.accept()
        try:
            print(f"\nTCP-Verbindung von {client_address}")

            # Empfange die Daten
            while True:
                data = connection.recv(2048)
                if data:
                    decoded_data = data.decode("utf-8", errors="ignore")
                    print(
                        f"(TCP) Empfangene Daten: {decoded_data} von {client_address}"
                    )
                else:
                    break
        finally:
            # Verbindung schließen
            connection.close()


def start_udp_server():
    # Erstelle einen UDP-Socket (AF_INET: IPv4, SOCK_DGRAM: UDP)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Binde den Socket an die Adresse (localhost) und Port (UDP_PORT)
    server_address = ("localhost", UDP_PORT)
    server_socket.bind(server_address)

    print(f"UDP-Server wartet auf eingehenden Traffic auf Port {UDP_PORT}...")

    while True:
        # Empfange die Daten
        data, client_address = server_socket.recvfrom(2048)
        decoded_data = data.decode("utf-8", errors="ignore")

        print(f"\n(UDP) Empfangene Daten: {decoded_data} von {client_address}")


if __name__ == "__main__":
    tcp_thread = threading.Thread(target=start_tcp_server)
    udp_thread = threading.Thread(target=start_udp_server)

    tcp_thread.start()
    udp_thread.start()

    tcp_thread.join()
    udp_thread.join()
