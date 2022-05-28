import uuid


class Traveller:
    __id = None
    __name = None
    __address = None
    __date_of_birth = None
    __contact = None
    __government_id = None
    __government_id_Type = None  # passport, driving license, national identity card, etc.
    __payments = []

    def __init__(self):
        self.__id = uuid.uuid4()

    def get_id(self):
        return self.__id

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_address(self, address):
        self.__address = address

    def get_address(self):
        return self.__address

    def set_date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth

    def get_date_of_birth(self):
        return self.__date_of_birth

    def set_contact(self, contact):
        self.__contact = contact

    def get_contact(self):
        return self.__contact

    def set_government_id(self, id, type):
        self.__government_id = id

    def get_government_id(self):
        return self.__government_id

    def set_government_id_type(self, type):
        self.__government_id_Type = type

    def get_government_id_type(self):
        return self.__government_id_Type

    def set_payments(self, payments):
        self.__payments = payments

    def add_payment(self, payment):
        self.__payments.append(payment)

    def get_payments(self):
        return self.__payments
