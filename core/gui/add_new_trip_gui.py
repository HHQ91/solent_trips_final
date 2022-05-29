from tkinter import Toplevel, Label, Button, Listbox, END, Scrollbar, RIGHT, Y
from tkinter.ttk import Entry, Combobox

from tkcalendar import DateEntry

from core.gui.add_new_traveller_gui import AddNewTravellerGUI
from core.gui.add_new_trip_leg_gui import AddNewTripLegGUI
from core.models.trip import Trip
from core.types.duration_types import DurationTypes
from core.types.role_types import RoleTypes


class AddNewTripGUI():
    def __init__(self, trips_gui):
        self.trips_gui = trips_gui
        self.trip = Trip(None, None, None, None, [], [])
        self.master = Toplevel()
        self.master.title("Add a trip")
        self.__add_name_label()
        self.__add_name_entry()
        self.__add_duration_label()
        self.__add_duration_entry()
        self.__add_start_date_label()
        self.__add_start_date_entry()
        self.__add_coordinator_label()
        self.__add_coordinator_entry()
        self.__add_coordinator_label()
        self.__add_coordinator_entry()
        self.__add_travellers_label()
        self.__add_travellers_entry()
        self.__add_new_traveller_button()
        self.__remove_selected_traveller_button()
        self.__add_trip_legs_label()
        self.__add_trip_legs_entry()
        self.__add_new_trip_legs_button()
        self.__remove_selected_trip_legs_button()
        self.__add_save_button()

    def __save(self):
        # get coordinator
        coordinator = [x for x in self.trips_gui.trip_system.users if self.coordinator_entry.get() in x.name][0]

        # save new trip
        self.trip.name = self.name_entry.get()
        self.trip.start_date = self.start_date_entry.get()
        self.trip.duration = DurationTypes[self.duration_entry.get()]
        self.trip.coordinator = coordinator
        print(self.trip.trip_legs)
        print(self.trip.travellers)
        self.trips_gui.trip_system.trips.append(self.trip)
        self.trips_gui.add_trip_info(self.trip)
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
        self.save_button.grid(row=10, column=1)

    def __add_coordinator_label(self):
        self.coordinator_label = Label(self.master)
        self.coordinator_label.grid(row=3, column=0, pady=5)
        self.coordinator_label.configure(text="Coordinator:")

    def __add_coordinator_entry(self):
        self.coordinator_entry = Combobox(self.master)
        self.coordinator_entry.grid(row=3, column=1)
        self.coordinator_entry["values"] = [x.name for x in self.trips_gui.trip_system.users if
                                            x.role is RoleTypes.coordinator]

    def __add_travellers_label(self):
        self.travellers_label = Label(self.master)
        self.travellers_label.grid(row=4, column=0, pady=5, rowspan=2)
        self.travellers_label.configure(text="Travellers:")

    def __add_travellers_entry(self):
        self.travellers_entry = Listbox(self.master, selectmode="multiple", exportselection=False)
        self.travellers_entry.grid(row=4, column=1, pady=5, rowspan=2)
        for traveller in self.trip.travellers:
            self.travellers_entry.insert(END, traveller.name)

    def __add_new_traveller_button(self):
        self.save_button = Button(self.master, text="Add New", command=self.__open_add_new_traveller)
        self.save_button.grid(row=4, column=2)

    def __remove_selected_traveller_button(self):
        self.save_button = Button(self.master, text="Remove Selected", command=self.__remove_selected_traveller)
        self.save_button.grid(row=5, column=2)

    def __open_add_new_traveller(self):
        self.add_new_traveller_gui = AddNewTravellerGUI(self)

    def __remove_selected_traveller(self):
        for i in self.travellers_entry.curselection():
            self.travellers_entry.delete(i)
            traveller = [x for x in self.trip.travellers if self.travellers_entry.get(i) in x.name][0]
            self.trip.travellers.remove(traveller)

    def __add_trip_legs_label(self):
        self.trip_legs_label = Label(self.master)
        self.trip_legs_label.grid(row=6, column=0, pady=5, rowspan=2)
        self.trip_legs_label.configure(text="Trip Legs:")

    def __add_trip_legs_entry(self):
        self.trip_legs_entry = Listbox(self.master, selectmode="multiple", exportselection=False)
        self.trip_legs_entry.grid(row=6, column=1, pady=5, rowspan=2)
        for trip_leg in self.trip.trip_legs:
            self.trip_legs_entry.insert(END, trip_leg.destination)

    def __add_new_trip_legs_button(self):
        self.save_button = Button(self.master, text="Add New", command=self.__open_add_new_trip_leg)
        self.save_button.grid(row=6, column=2)

    def __open_add_new_trip_leg(self):
        self.__open_add_new_trip_leg_gui = AddNewTripLegGUI(self)

    def __remove_selected_trip_legs_button(self):
        self.save_button = Button(self.master, text="Remove Selected", command=self.__remove_selected_trip_leg)
        self.save_button.grid(row=7, column=2)

    def __remove_selected_trip_leg(self):
        for i in self.trip_legs_entry.curselection():
            self.trip_legs_entry.delete(i)
            trip_legs = [x for x in self.trip.trip_legs if self.trip_legs_entry.get(i) in x.destination][0]
            self.trip.trip_legs.remove(trip_legs)

