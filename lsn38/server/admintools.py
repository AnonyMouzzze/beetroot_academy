from typing import Union

from data import ClientData


class AdminTools:
    def __init__(
        self, clients: list[ClientData], command: str, sender_data: ClientData
    ) -> None:
        self.__commands = {"/kick", "/makeadmin", "/removeadmin"}
        self.__command = command
        self.__clients = clients
        self.__sender_data = sender_data

    @staticmethod
    def is_admin(sender_data: ClientData) -> bool:
        return sender_data.admin

    def __client_exists(self, id: int) -> bool:
        for client in self.__clients:
            if client.id == id:
                return True
        return False

    def __id_validating(self, id: str) -> Union[bool, int]:
        try:
            uid = int(id)
            return uid
        except ValueError:
            return False

    def __kick_by_id(self, id: int) -> bool:
        uid = self.__id_validating(id)
        if uid and self.__client_exists(int(id)) and self.__clients[uid - 1].connection and not self.__clients[uid - 1].admin:
            self.__clients[uid - 1].connection.close()
            return True
        return False

    def __removeadmin_by_id(self, id) -> bool:
        if not self.__sender_data.id:
            uid = self.__id_validating(id)
            if uid and self.__client_exists(int(id)) and self.__clients[uid - 1].admin:
                self.__clients[uid - 1].admin = False
                return True
            return False
        return False

    def __makeadmin_by_id(self, id):
        uid = self.__id_validating(id)
        if uid and self.__client_exists(int(id)) and not self.__clients[uid - 1].admin:
            self.__clients[uid - 1].admin = True
            return True
        return False

    def command_executor(self) -> bool:
        command = self.__command.split(" ")
        if len(command) == 2:
            if command[0] == "/kick":
                return self.__kick_by_id(command[1])
            elif command[0] == "/makeadmin":
                return self.__makeadmin_by_id(command[1])
            elif command[0] == "/removeadmin":
                return self.__removeadmin_by_id(command[1])
