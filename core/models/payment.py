import uuid
from datetime import datetime


class Payment:
    id = None
    amount = None
    trip = None
    datetime = None

    def __init__(self, trip, amount):
        self.id = uuid.uuid4()
        self.trip = trip
        self.amount = amount
        self.datetime = datetime.now()

