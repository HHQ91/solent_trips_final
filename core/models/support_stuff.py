import uuid


class SupportStuff:
    id = None
    name = None

    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name