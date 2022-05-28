import uuid
from datetime import datetime


class Payment:
    __id = None
    __passenger = None
    __trip = None
    __datetime = None

    def __init__(self, trip, passenger):
        self.__id = uuid.uuid4()
        self.__trip = trip
        self.__passenger = passenger
        self.__datetime = datetime.now()

    def get_id(self):
        return self.__id

    def get_passenger(self):
        return self.__passenger

    def get_trip(self):
        return self.__trip
