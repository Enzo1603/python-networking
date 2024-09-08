import socket
import threading

from flask import Flask, render_template_string

FLASK_PORT = 7000
TCP_PORT = 7001
UDP_PORT = 7002
HTML_TEMPLATE = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Eingehende Daten</title>
    </head>
    <body>
        <h1>Dynamische Anzeige des eingehenden Traffics</h1>
        <ul>
            {% for entry in data %}
            <li>{{ entry }}</li>
            {% endfor %}
        </ul>
    </body>
    </html>
    """


app = Flask(__name__)
current_data = []


# Funktion, die dynamisch die empfangenen Daten auf der Webseite anzeigt
@app.route("/")
def home():
    global current_data

    # Rückgabe der HTML-Seite mit den eingehenden Daten
    rendered_html = render_template_string(HTML_TEMPLATE, data=current_data)
    current_data = []  # Leeren des Zwischenspeichers nach dem Rendern
    return rendered_html


# Einen einfachen TCP-Server erstellen
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
            print(f"TCP-Verbindung von {client_address}")

            # Empfange die Daten
            while True:
                data = connection.recv(2048)
                if data:
                    decoded_data = data.decode("utf-8", errors="ignore")
                    print(
                        f"(TCP) Empfangene Daten: {decoded_data} von {client_address}"
                    )
                    current_data.append(decoded_data)
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

        print(f"(UDP) Empfangene Daten: {decoded_data} von {client_address}")

        current_data.append(decoded_data)


if __name__ == "__main__":
    tcp_thread = threading.Thread(target=start_tcp_server)
    tcp_thread.daemon = True
    tcp_thread.start()

    udp_thread = threading.Thread(target=start_udp_server)
    udp_thread.daemon = True
    udp_thread.start()

    app.run(debug=True, port=FLASK_PORT, host="0.0.0.0")
