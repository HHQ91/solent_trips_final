import uuid


class User:
    id = None
    name = None
    password = None
    role = None  # Trip Coordinator, Trip Manager, Administrator

    def __init__(self, name, password, role):
        self.id = uuid.uuid4()
        self.name = name
        self.password = password
        self.role = role
