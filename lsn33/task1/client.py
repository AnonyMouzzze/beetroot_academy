import socket

server_address = ('127.0.0.1', 8080)

UDPClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

UDPClient.sendto(b'Hello Server', server_address)
data = UDPClient.recvfrom(1024)[0]
print(data)