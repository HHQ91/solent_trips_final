import uuid


class Trip:
    id = None
    name = None
    start_date = None
    duration = None  # will be on day, weekend, tonight
    coordinator = None
    travellers = []
    trip_legs = []
    support_stuffs = []

    def __init__(self, name, start_date, duration):
        self.id = uuid.uuid4()
        self.name = name
        self.start_date = start_date
        self.duration = duration

    def assign_coordinator(self, coordinator):
        self.coordinator = coordinator

    def add_traveller(self, traveller):
        self.travellers.append(traveller)

    def remove_traveller(self, id):
        for i in self.travellers:
            if i.id is id:
                self.travellers.remove(i)

    def assign_travellers(self, travellers):
        self.travellers = travellers

    def add_trip_leg(self, trip_leg):
        self.trip_legs.append(trip_leg)

    def remove_trip_leg(self, id):
        for i in self.trip_legs:
            if i.id is id:
                self.trip_legs.remove(i)

    def assign_trip_legs(self, trip_legs):
        self.trip_legs = trip_legs

    def add_support_stuff(self, support_stuff):
        self.support_stuffs.append(support_stuff)

    def remove_support_stuff(self, id):
        for i in self.support_stuffs:
            if i.id is id:
                self.support_stuffs.remove(i)

    def assign_support_stuffs(self, support_stuffs):
        self.support_stuffs = support_stuffs
