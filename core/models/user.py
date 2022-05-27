import uuid


class User:
    __id = None
    __name = None
    __password = None
    __role = None  # Trip Coordinator, Trip Manager, Administrator

    def __init__(self, name, password, role):
        self.__id = uuid.uuid4()
        self.__name = name
        self.__password = password
        self.__role = role

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_password(self):
        return self.__password

    def get_role(self):
        return self.__role
