from core.models.trip import Trip
from core.models.user import User
from core.types.role_types import RoleTypes


class TripSystem:
    __trips = []
    __users = []

    def __init__(self):
        # add system users
        self.__users.append(User("TripCoordinator", "12345", RoleTypes.coordinator))
        self.__users.append(User("TripManager", "12345", RoleTypes.manager))
        self.__users.append(User("TripAdmin", "12345", RoleTypes.administrator))

    def get_trips(self):
        return self.__trips

    def add_trip(self, name, duration, start_date, coordinator, travellers, tip_legs):
        trip = Trip()
        trip.set_name(name)
        trip.set_duration(duration)
        trip.set_start_date(start_date)
        trip.set_coordinator(coordinator)
        trip.set_travellers(travellers)
        trip.set_tip_legs(tip_legs)
        # add the new trip
        self.__trips.append(trip)

    def update_trip(self, id, name, duration, start_date, coordinator, travellers, tip_legs):
        for i, item in self.__trips:
            if item.get_id() == id:
                if name is not None:
                    self.__trips[i].set_name(name)
                if duration is not None:
                    self.__trips[i].set_duration(duration)
                if start_date is not None:
                    self.__trips[i].set_start_date(start_date)
                if coordinator is not None:
                    self.__trips[i].set_coordinator(coordinator)
                if travellers is not None:
                    self.__trips[i].set_travellers(travellers)
                if tip_legs is not None:
                    self.__trips[i].set_tip_legs(tip_legs)
                break

    def delete_trip(self, id):
        for i, item in self.__trips:
            if item.get_id() == id:
                self.__trips.remove(item)


