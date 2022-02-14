import socket

LOCAL_HOST = '127.0.0.1'
LOCAL_PORT = 8080

UDPServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDPServer.bind((LOCAL_HOST, LOCAL_PORT))

while True:
    data, address = UDPServer.recvfrom(1024)
    print(f'Client address:{address}\nClient data: {data}')
    UDPServer.sendto(b'Hello client', address)