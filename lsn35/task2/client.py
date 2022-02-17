import socket

TARGET = ("127.0.0.1", 8080)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(TARGET)
    sock.sendall(b"hello")
    print(repr(sock.recv(1024)))
