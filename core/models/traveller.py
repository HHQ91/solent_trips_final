import uuid


class Traveller:
    id = None
    name = None
    address = None
    date_of_birth = None
    contact = None
    government_id = None
    government_id_Type = None  # passport, driving license, national identity card, etc.
    payments = []

    def __init__(self, name, address, date_of_birth, contact, government_id, government_id_type, payments):
        self.__id = uuid.uuid4()
        self.name = name
        self.address = address
        self.date_of_birth = date_of_birth
        self.contact = contact
        self.government_id = government_id
        self.government_id_type = government_id_type
        self.payments = payments
