import uuid


class Passenger:
    __id = None
    __name = None

    def __init__(self):
        self.__id = uuid.uuid4()

    def get_id(self):
        return self.__id

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
