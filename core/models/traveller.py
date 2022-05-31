import uuid


class Traveller:
    id = None
    name = None
    address = None
    date_of_birth = None
    contact = None
    government_id = None
    government_id_type = None  # passport, driving license, national identity card, etc.
    payments = []

    def __init__(self, name, address, date_of_birth, contact):
        self.id = uuid.uuid4()
        self.name = name
        self.address = address
        self.date_of_birth = date_of_birth
        self.contact = contact

    def add_payment(self, payment):
        self.payments.append(payment)

    def remove_payment(self, id):
        for i in self.payments:
            if i.id is id:
                self.payments.remove(i)

    def assign_payments(self, payments):
        self.payments = payments

    def add_government_id(self, id, type):
        self.government_id = id
        self.government_id_type = type
