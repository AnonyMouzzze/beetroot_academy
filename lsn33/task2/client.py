import socket

HOST = '127.0.0.1'  
PORT = 8080        

string = input('Input a string to encode:' )
key = input('Enter a specific key: ')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(f'{string}:{key}'.encode())
    data = s.recv(1024)

print('Received', repr(data))