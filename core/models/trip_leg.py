import uuid


class TripLeg:
    id = None
    start_location = None
    destination = None
    mode_of_transport = None  # plane, ferry, coach, or taxi

    def __init__(self, start_location, destination, mode_of_transport):
        self.id = uuid.uuid4()
        self.start_location = start_location
        self.destination = destination,
        self.mode_of_transport = mode_of_transport

