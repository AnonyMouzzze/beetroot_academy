import socket
from dataclasses import dataclass


@dataclass
class ClientData:
    nickname: str
    connection: socket.socket
    id: int
    admin: bool = False
