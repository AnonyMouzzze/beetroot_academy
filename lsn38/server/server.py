import socket
import threading

from admintools import AdminTools
from data import ClientData


class Server:
    def __init__(
        self, ip: str, port: int, server_name="server", max_connections_queue: int = 1
    ) -> None:
        self._server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server_socket.bind((ip, port))
        self._server_socket.listen(max_connections_queue)
        self._server = ClientData(server_name, None, 0, True)
        self._clients = []

    def _client_handler(self, connection: socket.socket) -> None:
        client_data = self._find_client_data_by_connection(connection)
        while True:
            try:
                message = connection.recv(1024)
                if not message:
                    continue
                self._message_checking(client_data, message.decode())
            except (OSError, ConnectionAbortedError, ConnectionResetError):
                print(f"{client_data.nickname} disconnected")
                self._brake_connection_with(client_data)
                break

    def _brake_connection_with(self, client_data: ClientData) -> None:
        index = self._clients.index(client_data)
        self._clients[index].connection = None

    def _find_client_data_by_connection(self, connection: socket.socket) -> ClientData:
        for data in self._clients:
            data: ClientData
            if data.connection == connection:
                return data

    def _transform_message(self, client_data: ClientData, message: str) -> str:
        return f"{client_data.nickname}({client_data.id}): {message}"

    def _send_message_to_all(self, sender_data: ClientData, message: str) -> None:
        transformed_message = self._transform_message(sender_data, message)
        print(transformed_message)
        for client in self._clients:
            client: ClientData
            if client.connection:
                client.connection.sendall(transformed_message.encode())

    def _create_new_connection_thread(self, connection: socket.socket) -> None:
        client_connection_thread = threading.Thread(
            target=self._client_handler, args=(connection,)
        )
        client_connection_thread.start()
        return client_connection_thread

    def _get_new_client_name(self, connection: socket.socket) -> str:
        while True:
            try:
                nickname = connection.recv(64).decode()
                print(nickname)
                if 3 <= len(nickname) <= 16:
                    connection.sendall(b'True')
                    return nickname
                connection.sendall(b'False')
                connection.close()
            except (OSError, ConnectionAbortedError, ConnectionResetError):
                break

    def _add_new_client_data(self, nickname: str, connection: socket.socket) -> None:
        for client in self._clients:
            client: ClientData
            if not client.connection:
                free_slot_index = self._clients.index(client)
                self._clients.insert(free_slot_index, ClientData(nickname, connection, client.id))
                self._clients.remove(client)
                print(self._clients)
                return

        self._clients.append(ClientData(nickname, connection, len(self._clients) + 1))
        print(self._clients)

    def _create_new_client(self, connection: socket.socket) -> None:
        nickname = self._get_new_client_name(connection)
        if nickname:
            self._add_new_client_data(nickname, connection)
            self._create_new_connection_thread(connection)

    def _create_server_terminal(self):
        thread = threading.Thread(target=self._server_messages_handler)
        thread.start()

    def _message_checking(self, sender_data: ClientData, message: str) -> None:
        if message.startswith("/"):
            if AdminTools.is_admin(sender_data):
                admintools = AdminTools(self._clients, message, sender_data)
                print(admintools.command_executor())
            else:
                sender_data.connection.sendall(b"No permission")
        else:
            self._send_message_to_all(sender_data, message)

    def _server_messages_handler(self):
        while True:
            message = input()
            self._message_checking(self._server, message)

    def run(self) -> None:
        self._create_server_terminal()
        while True:
            connection, _ = self._server_socket.accept()
            self._create_new_client(connection)