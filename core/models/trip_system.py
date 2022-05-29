from datetime import datetime
from tkinter import Tk

from core.gui.login_gui import LoginGUI
from core.gui.trips_gui import TripsGUI
from core.models.traveller import Traveller
from core.models.trip import Trip
from core.models.trip_leg import TripLeg
from core.models.user import User
from core.types.duration_types import DurationTypes
from core.types.role_types import RoleTypes
from core.types.trasport_mode_types import TransportModeTypes


class TripSystem:
    trips = []
    users = []
    travellers = []
    logged_in_user = None
    app_name = "Trips Management System"

    def __init__(self):
        self.__add_demo_data()
        # initial the tkinter
        self.root = Tk()
        self.root.wm_title(self.app_name)
        # add the login gui
        self.login_gui = LoginGUI(self.root, self)
        # ---
        self.root.mainloop()

    def get_trips(self):
        trips = []
        # coordinator will see only the trip that assign to him
        if self.logged_in_user == RoleTypes.coordinator:
            for i, trip in self.trips:
                trips.append(trip)
        else:
            trips = self.trips
        return trips

    def add_trip(self, name, duration, start_date, coordinator, travellers, trip_legs):
        self.__accepted_role_or_throw_exception(RoleTypes.manager)
        trip = Trip(name, start_date, duration, coordinator, travellers, trip_legs)
        # add the new trip
        self.trips.append(trip)

    def update_trip(self, id, name, duration, start_date, coordinator, travellers, trip_legs):
        self.__accepted_role_or_throw_exception(RoleTypes.manager)
        for i, item in self.trips:
            if item.id == id:
                if name is not None:
                    self.trips[i].name = name
                if duration is not None:
                    self.trips[i].duration = duration
                if start_date is not None:
                    self.trips[i].start_date = start_date
                if coordinator is not None:
                    self.trips[i].coordinator = coordinator
                if travellers is not None:
                    self.trips[i].travellers = travellers
                if trip_legs is not None:
                    self.trips[i].trip_legs = trip_legs
                break

    def delete_trip(self, id):
        self.__accepted_role_or_throw_exception(RoleTypes.manager)
        for i, item in self.trips:
            if item.get_id() == id:
                self.trips.remove(item)

    def logging_in(self, username, password):
        for user in self.users:
            if user.name == username and user.password == password:
                self.logged_in_user = user
                self.login_gui.__del__()
                self.trips_gui = TripsGUI(self.root, self)
                break
        # if logged-in user still null then throw an exception
        if self.logged_in_user is None:
            raise Exception("Please use a valid account")

    # logged in accepted role to perform the action
    def __accepted_role_or_throw_exception(self, accepted_role):
        if accepted_role is RoleTypes.coordinator:
            return
        if accepted_role is RoleTypes.manager and (self.logged_in_user.get_role() is RoleTypes.manager or
                                                   self.logged_in_user.get_role() is RoleTypes.administrator):
            return
        if accepted_role is RoleTypes.administrator and self.logged_in_user.get_role() is RoleTypes.administrator:
            return

        raise Exception("Not allowed to perform this action")

    def __add_demo_data(self):
        # add system users
        self.users.append(User("coordinator1", "12345", RoleTypes.coordinator))
        self.users.append(User("coordinator2", "12345", RoleTypes.coordinator))
        self.users.append(User("coordinator3", "12345", RoleTypes.coordinator))
        self.users.append(User("manager", "12345", RoleTypes.manager))
        self.users.append(User("a", "a", RoleTypes.administrator))
        # add demo trip
        demo_trip1 = Trip("Trip to turkey", datetime.now(), DurationTypes.weekend, self.users[0], None, None)
        self.trips.append(demo_trip1)
        self.trips.append(demo_trip1)
        self.trips.append(demo_trip1)
        self.trips.append(demo_trip1)
        self.trips.append(demo_trip1)
        self.trips.append(demo_trip1)
        self.trips.append(demo_trip1)


