from tkinter import ttk, StringVar, Label, Button, Toplevel
from tkinter.ttk import Entry, Frame, Separator, Combobox
from tkcalendar import DateEntry

from core.gui.add_new_trip_gui import AddNewTripGUI
from core.models.trip import Trip
from core.types.duration_types import DurationTypes


class TripsGUI():

    def __init__(self, master, trip_system):
        self.trip_system = trip_system
        self.master = master
        self.__add_header_label()
        self.__add_new_trip_button()
        self.trip_info_widgets = []
        self.__add_trips_info()

    def __add_header_label(self):
        self.username_label = Label()
        self.username_label.pack()
        self.username_label.configure(text="Trips", font="Helvetica 18 bold")

    def __add_trips_info(self):
        for i, trip in enumerate(self.trip_system.get_trips()):
            self.add_trip_info(trip)

    def add_trip_info(self, trip):
        Separator(orient='horizontal').pack(fill='x')
        trip_info = f"Trip: {trip.name}, duration: {trip.duration.name}, start in: {trip.start_date}"
        trip_name_label = Label()
        trip_name_label.pack()
        trip_name_label.configure(text=trip_info)
        self.trip_info_widgets.append(trip_name_label)

    def __add_new_trip_button(self):
        self.add_new_trip_button = Button()
        self.add_new_trip_button.configure(text="Add New Trip", command=self.__open_add_new_trip)
        self.add_new_trip_button.pack(padx=10)

    def __open_add_new_trip(self):
        self.add_new_trip_gui = AddNewTripGUI(self)
