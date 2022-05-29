from tkinter import Toplevel, Label, Button
from tkinter.ttk import Entry, Combobox

from tkcalendar import DateEntry

from core.models.trip import Trip
from core.types.duration_types import DurationTypes


class AddNewTripGUI():

    def __init__(self, trips_gui):
        self.trips_gui = trips_gui

        self.master = Toplevel()
        self.master.title("Add a trip")
        self.__add_name_label()
        self.__add_name_entry()
        self.__add_duration_label()
        self.__add_duration_entry()
        self.__add_start_date_label()
        self.__add_start_date_entry()
        self.__add_save_button()

    def __save(self):
        trip = Trip(
            self.name_entry.get(),
            self.start_date_entry.get(),
            DurationTypes[self.duration_entry.get()],
            None, None, None)
        print(trip.duration)
        self.trips_gui.trip_system.trips.append(trip)
        self.trips_gui.add_trip_info(trip)
        self.master.destroy()

    def __add_name_label(self):
        self.name_label = Label(self.master)
        self.name_label.grid(row=0, column=0, pady=5)
        self.name_label.configure(text="Name:")

    def __add_name_entry(self):
        self.name_entry = Entry(self.master)
        self.name_entry.grid(row=0, column=1, pady=5)

    def __add_duration_label(self):
        self.duration_label = Label(self.master)
        self.duration_label.grid(row=1, column=0, pady=5)
        self.duration_label.configure(text="Duration:")

    def __add_duration_entry(self):
        self.duration_entry = Combobox(self.master, values=(
            DurationTypes.weekend.name, DurationTypes.one_day.name, DurationTypes.fortnight.name))
        self.duration_entry.grid(row=1, column=1)

    def __add_start_date_label(self):
        self.start_date_label = Label(self.master)
        self.start_date_label.grid(row=2, column=0, pady=5)
        self.start_date_label.configure(text="Start date:")

    def __add_start_date_entry(self):
        self.start_date_entry = DateEntry(self.master)
        self.start_date_entry.grid(row=2, column=1)

    def __add_save_button(self):
        self.save_button = Button(self.master, text="Save", command=self.__save)
        self.save_button.grid(row=3, column=1)
