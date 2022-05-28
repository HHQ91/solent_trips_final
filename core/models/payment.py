import uuid
from datetime import datetime


class Payment:
    __id = None
    __traveller = None
    __trip = None
    __datetime = None

    def __init__(self, trip, traveller):
        self.__id = uuid.uuid4()
        self.__trip = trip
        self.__traveller = traveller
        self.__datetime = datetime.now()

    def get_id(self):
        return self.__id

    def get_traveller(self):
        return self.__traveller

    def get_trip(self):
        return self.__trip
