import sys

from PyQt5.QtWidgets import QApplication

from interfaceinit import ChatInterface, LoginInterface


class InterfaceControll:
    def __init__(self) -> None:
        self._app = QApplication(sys.argv)

    def execute_application(self) -> None:
        sys.exit(self._app.exec())

    def close_current_window(self) -> None:
        self.current_interface.close()

    def draw_login_interface(self) -> None:
        self.current_interface = LoginInterface()
        self.current_interface.show()

    def draw_chat_interface(self) -> None:
        self.close_current_window()
        self.current_interface = ChatInterface()
        self.current_interface.show()