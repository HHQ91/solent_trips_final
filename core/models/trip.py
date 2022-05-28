import uuid


class Trip:
    __id = None
    __name = None
    __start_date = None
    __duration = None  # will be on day, weekend, tonight
    __coordinator = None
    __travellers = []
    __tip_legs = []

    def __init__(self):
        self.__id = uuid.uuid4()

    def get_id(self):
        return self.__id

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_start_date(self, date):
        self.__start_date = date

    def get_start_date(self):
        return self.__start_date

    def set_duration(self, duration):
        self.__duration = duration

    def get_duration(self):
        return self.__duration

    def set_coordinator(self, coordinator):
        self.__coordinator = coordinator

    def get_coordinator(self):
        return self.__coordinator

    def set_travellers(self, travellers):
        self.__travellers = travellers

    def add_traveller(self, traveller):
        self.__travellers.append(traveller)

    def get_travellers(self):
        return self.__travellers

    def set_tip_legs(self, tip_legs):
        self.__tip_legs = tip_legs

    def add_tip_leg(self, tip_leg):
        self.__tip_legs.append(tip_leg)

    def get_tip_legs(self):
        return self.__tip_legs
