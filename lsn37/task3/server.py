import socket
import asyncio


HOST = "127.0.0.1"
PORT = 8180


async def client_handler(connection):
    loop = asyncio.get_event_loop()
    data = None
    while data != "quit":
        data = (await loop.sock_recv(connection, 1024)).decode()
        await loop.sock_sendall(connection, data.upper().encode())
        if not data:
            connection.close()
            break


async def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(8)
    server.setblocking(False)

    loop = asyncio.get_event_loop()
    while True:
        connection, _ = await loop.sock_accept(server)
        await client_handler(connection)


asyncio.run(main())
