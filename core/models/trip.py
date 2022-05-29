import uuid


class Trip:
    id = None
    name = None
    start_date = None
    duration = None  # will be on day, weekend, tonight
    coordinator = None
    travellers = []
    trip_legs = []

    def __init__(self):
        self.id = uuid.uuid4()

    def __init__(self, name, start_date, duration, coordinator, travellers, trip_legs):
        self.id = uuid.uuid4()
        self.name = name
        self.start_date = start_date
        self.duration = duration
        self.coordinator = coordinator
        self.travellers = travellers
        self.trip_legs = trip_legs

