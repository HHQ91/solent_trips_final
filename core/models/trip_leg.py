import uuid


class TripLeg:
    __id = None
    __start_location = None
    __destination = None
    __mode_of_transport = None  # plane, ferry, coach, or taxi

    def __init__(self):
        self.__id = uuid.uuid4()

    def get_id(self):
        return self.__id

    def set_start_location(self, start_location):
        self.__start_location = start_location

    def get_start_location(self):
        return self.__start_location

    def set_destination(self, start_location):
        self.__start_location = start_location

    def get_destination(self):
        return self.__start_location

    def set_mode_of_transport(self, mode_of_transport):
        self.__mode_of_transport = mode_of_transport

    def get_mode_of_transport(self):
        return self.__mode_of_transport
