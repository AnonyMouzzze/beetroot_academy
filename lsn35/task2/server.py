import socket
import threading


def client_handler(connection):
    try:
        while True:
            data = connection.recv(1024)
            print(f"Received data: {data}")
            if not data:
                break
            connection.sendall(data.upper())
    finally:
        connection.close()


HOST = "127.0.0.1"
PORT = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(5)
while True:
    connection, client_address = sock.accept()
    thread = threading.Thread(target=client_handler, args=(connection,))
    thread.start()
