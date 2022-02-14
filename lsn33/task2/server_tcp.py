import socket
from string import ascii_lowercase
from typing import Union

def caesar(string: str, key: int) -> str:
    string = string.lower().strip()
    letters = ascii_lowercase
    res = ''

    if not string.isalpha():
        return 'Use only letters'
    elif type(key) != int:
        try:
            key = int(key)
        except ValueError:
            return 'Invlaid Key'
    if key >= len(letters) - 1:
        return f'Key must be lower tnan {len(letters) - 1}'

    for letter in string:
        letter_index = letters.index(letter)
        if letter_index + key > len(letters) - 1:
            res += letters[letter_index + key - len(letters) - 1]
        else:
            res += letters[letter_index + key]
    return res

def validate_data(string: str) -> Union[tuple, bool]:
    data = string.split(':')
    if len(data) == 2:
        return tuple(data)
    return False

HOST = '127.0.0.1'
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

while True:
    connection , client_address = server.accept()
    try:
        print(f'{client_address[0]} connected with port {client_address[1]}')
        while True:
            data = connection.recv(1024).decode()
            if validate_data(data):
                data = tuple(data.split(':'))
                connection.sendall(caesar(*data).encode())
            else:
                connection.sendall(b'Invalid format string:key')
                break
    finally:
        connection.close()