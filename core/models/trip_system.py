from tkinter import Tk

from core.gui.login_gui import LoginGUI
from core.gui.trips_gui import TripsGUI
from core.models.trip import Trip
from core.models.user import User
from core.types.role_types import RoleTypes


class TripSystem:
    __trips = []
    __users = []
    __logged_in_user = None
    __app_name = "Trips Management System"

    def __init__(self):
        # add system users
        self.__users.append(User("coordinator", "12345", RoleTypes.coordinator))
        self.__users.append(User("manager", "12345", RoleTypes.manager))
        self.__users.append(User("admin", "12345", RoleTypes.administrator))
        # initial the tkinter
        self.root = Tk()
        self.root.wm_title(self.__app_name)
        # add the login gui
        self.login_gui = LoginGUI(self.root, self)
        # ---
        self.root.mainloop()


    def get_trips(self):
        trips = []
        # coordinator will see only the trip that assign to him
        if self.__logged_in_user == RoleTypes.coordinator:
            for i, trip in self.__trips:
                trips.append(trip)
        else:
            trips = self.__trips
        return trips

    def add_trip(self, name, duration, start_date, coordinator, travellers, tip_legs):
        self.__accepted_role_or_throw_exception(RoleTypes.manager)
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
        self.__accepted_role_or_throw_exception(RoleTypes.manager)
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
        self.__accepted_role_or_throw_exception(RoleTypes.manager)
        for i, item in self.__trips:
            if item.get_id() == id:
                self.__trips.remove(item)

    def logging_in(self, username, password):
        for user in self.__users:
            if user.get_name() == username and user.get_password() == password:
                self.__logged_in_user = user
                self.login_gui.__del__()
                self.trips_gui = TripsGUI(self.root, self)
                break
        # if logged-in user still null then throw an exception
        if self.__logged_in_user is None:
            raise Exception("Please use a valid account")

    # logged in accepted role to perform the action
    def __accepted_role_or_throw_exception(self, accepted_role):
        if accepted_role is RoleTypes.coordinator:
            return
        if accepted_role is RoleTypes.manager and (self.__logged_in_user.get_role() is RoleTypes.manager or
                                          self.__logged_in_user.get_role() is RoleTypes.administrator):
            return
        if accepted_role is RoleTypes.administrator and self.__logged_in_user.get_role() is RoleTypes.administrator:
            return

        raise Exception("Not allowed to perform this action")
