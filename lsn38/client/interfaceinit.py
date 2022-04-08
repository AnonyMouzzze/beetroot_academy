import socket
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from designerinterface.designerchatinterface import Ui_MainWindow as Ui_ChatWindow
from designerinterface.designerlogininterface import Ui_MainWindow as Ui_LoginWindow
from threadutil import run_in_main_thread


class LoginInterface(QMainWindow, Ui_LoginWindow):
    def __init__(self):
        super(LoginInterface, self).__init__()
        self.setupUi(self)

    def connect_login_button_signal(self, func) -> None:
        self.login_button.clicked.connect(func)

    def set_invalid_nickname_message(self) -> None:
        self.input_nickname.setText('Invalid nickname')

    def set_invalid_ip_address_message(self) -> None:
        self.input_ip_address.setText('Invalid IP address')
    
    def get_user_input(self) -> tuple[str, str]:
        address = self.input_ip_address.text()
        nickname = self.input_nickname.text()
        return (address, nickname)


class ChatInterface(QMainWindow, Ui_ChatWindow):
    def __init__(self):
        super(ChatInterface, self).__init__()
        self.setupUi(self)
        self.client_socket: socket.socket = None
        
    def clear_message_input(self) -> None:
        self.input_message.setText('')
    
    def get_message_from_input(self) -> str:
        message = self.input_message.text()
        self.clear_message_input()
        return message

    def display_new_message(self, message: str) -> None:
        self._append_message = run_in_main_thread(self.show_messages_area.appendPlainText)
        self._append_message(message)

    def connect_send_message_button_signal(self, func) -> None:
        self.send_message_button.clicked.connect(func)
        self.input_message.returnPressed.connect(func)     

    def closeEvent(self, event) -> None:
        '''Overloaded method'''
        close_window_request = QMessageBox.question(self, 'Quit', 'Are you sure want to disconnect from chat?', QMessageBox.Yes | QMessageBox.No)

        if close_window_request == QMessageBox.Yes:
            event.accept()
            self.client_socket.close()
        else:
            event.ignore()