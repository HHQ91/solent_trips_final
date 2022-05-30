from datetime import datetime
from tkinter import Tk
from core.gui.login_gui import LoginGUI
from core.gui.trips_gui import TripsGUI
from core.models.trip import Trip
from core.models.user import User
from core.types.duration_types import DurationTypes
from core.types.role_types import RoleTypes


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
    def accepted_role_or_throw_exception(self, accepted_role):
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
        demo_trip1 = Trip("Trip to turkey 1", datetime.now(), DurationTypes.weekend)
        demo_trip1.assign_coordinator(self.users[0])
        demo_trip2 = Trip("Trip to turkey 2", datetime.now(), DurationTypes.weekend)
        demo_trip2.assign_coordinator(self.users[2])
        self.trips.append(demo_trip1)
        self.trips.append(demo_trip2)



