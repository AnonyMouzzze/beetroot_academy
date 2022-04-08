import socket
import threading

from interfacecontroll import InterfaceControll


class Client:
    def _start_login_window(self) -> None:
        self._userinterface = InterfaceControll()
        self._userinterface.draw_login_interface()
        self._userinterface.current_interface.connect_login_button_signal(self._connect_to_server)
        self._userinterface.execute_application()

    def _start_chat_window(self) -> None:
        message_receiver_thread = threading.Thread(target=self._receive_message_from_server)
        message_receiver_thread.start()
        self._userinterface.draw_chat_interface()

        self._userinterface.current_interface.client_socket = self._client_socket
        self._userinterface.current_interface.connect_send_message_button_signal(self._message_send_pressed)

    def _connect_to_server(self) -> None:
        address, nickname = self._userinterface.current_interface.get_user_input()

        if not self._try_make_connection(address):
            return
        
        if 3 <= len(nickname) <= 16:
            self._send_nickname_to_server(nickname)
            self._start_chat_window()
            return

        self._userinterface.current_interface.set_invalid_nickname_message()

    def _try_make_connection(self, address: str) -> bool:
        try:
            ip = address.split(':')[0]
            port = int(address.split(':')[1])
            self._client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._client_socket.connect((ip, port))
        except (IndexError, ConnectionRefusedError, TimeoutError):
            self._userinterface.current_interface.set_invalid_ip_address_message()
            return False
        return True

    def _send_nickname_to_server(self, nickname: str) -> bool:
        self._client_socket.sendall(nickname.encode())
        server_accept = self._client_socket.recv(1024).decode()
        return bool(server_accept)

    def _message_send_pressed(self):
        message = self._userinterface.current_interface.get_message_from_input()
        self._send_message_to_server(message)
        
    def _send_message_to_server(self, message: str) -> None:
        self._client_socket.sendall(message.encode())

    def _receive_message_from_server(self) -> str:
        while True:
            try:
                message = self._client_socket.recv(1024)
                if message:
                    self._userinterface.current_interface.display_new_message(message.decode())
                    print(message.decode())
            except (OSError, ConnectionResetError):
                self._client_socket.close()
                self._userinterface.close_current_window()
                break

    def start(self) -> None:
        self._start_login_window()
        