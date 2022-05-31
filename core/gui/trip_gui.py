from tkinter import Toplevel, Label, Button, Listbox, END, Scrollbar, RIGHT, Y, messagebox
from tkinter.ttk import Entry, Combobox, Separator

from tkcalendar import DateEntry

from core.gui.coordinator_gui import CoordinatorGUI
from core.gui.add_new_traveller_gui import AddNewTravellerGUI
from core.gui.add_new_trip_leg_gui import AddNewTripLegGUI
from core.models.trip import Trip
from core.types.duration_types import DurationTypes
from core.types.role_types import RoleTypes


class TripGUI():
    def __init__(self, trips_gui, trip=None):
        self.trips_gui = trips_gui
        if trip is not None:
            self.mode = "Edit"
            self.trip = trip
        else:
            self.mode = "Add"
            self.trip = Trip(None, None, None)
        self.master = Toplevel()
        self.master.title(f"{self.mode} a trip")
        self.__add_name_label()
        self.__add_name_entry()
        self.__add_duration_label()
        self.__add_duration_entry()
        self.__add_start_date_label()
        self.__add_start_date_entry()
        self.__add_separator()

        # when the user is coordinator so no need to the coordinator entry
        if self.trips_gui.trip_system.is_accepted_role(RoleTypes.manager):
            self.__add_coordinator_label()
            self.__add_coordinator_entry()
            self.__add_coordinator_label()
            self.__add_coordinator_entry()
            self.__add_new_coordinator_button()
            self.__add_remove_coordinator_button()
            self.__edit_selected_coordinator_button()
            self.__add_separator()

        self.__add_travellers_label()
        self.__add_travellers_entry()
        self.__add_new_traveller_button()
        self.__remove_selected_traveller_button()
        #self.__edit_selected_traveller_button()
        self.__add_separator()

        self.__add_trip_legs_label()
        self.__add_trip_legs_entry()
        self.__add_new_trip_legs_button()
        self.__remove_selected_trip_legs_button()
        #self.__edit_selected_trip_legs_button()
        self.__add_separator()

        self.__add_save_button()

    def __save(self):

        # save new trip
        if self.trips_gui.trip_system.is_accepted_role(RoleTypes.manager):
            self.trip.name = self.name_entry.get()
            if not self.trip.name:
                return messagebox.showerror("Add Failed", "Please enter a valid name")

            self.trip.start_date = self.start_date_entry.get()

            self.trip.duration = DurationTypes[self.duration_entry.get()]
            if not self.trip.duration:
                return messagebox.showerror("Add Failed", "Please select a valid duration")
            # get coordinator
            if len(self.coordinator_entry.curselection()) <= 0:
                return messagebox.showerror("Add Failed", "Please select a valid coordinator")
            coordinator = [x for x in self.trips_gui.trip_system.users if
                           self.coordinator_entry.get(self.coordinator_entry.curselection()[0]) in x.name][0]
            self.trip.assign_coordinator(coordinator)
        if self.mode == "Edit":
            for i, trip in enumerate(self.trips_gui.trip_system.trips):
                if trip.id == self.trip.id:
                    self.trips_gui.trip_system.trips[i] = self.trip
                    self.trips_gui.update_trips_info()

        else:
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
        # for edit view mode
        if self.trip.name is not None:
            self.name_entry.insert(0, self.trip.name)
        self.name_entry.config(state= "disabled")


    def __add_duration_label(self):
        self.duration_label = Label(self.master)
        self.duration_label.grid(row=1, column=0, pady=5)
        self.duration_label.configure(text="Duration:")

    def __add_duration_entry(self):
        self.duration_entry = Combobox(self.master, values=(
            DurationTypes.one_day.name, DurationTypes.weekend.name, DurationTypes.fortnight.name))
        self.duration_entry.grid(row=1, column=1)
        # for edit view mode
        if self.trip.duration is not None:
            self.duration_entry.current(self.trip.duration.value - 1)
        self.duration_entry.config(state= "disabled")

    def __add_start_date_label(self):
        self.start_date_label = Label(self.master)
        self.start_date_label.grid(row=2, column=0, pady=5)
        self.start_date_label.configure(text="Start date:")

    def __add_start_date_entry(self):
        self.start_date_entry = DateEntry(self.master)
        self.start_date_entry.grid(row=2, column=1)
        # for edit view mode
        if self.trip.start_date is not None:
            self.start_date_entry.insert(0, self.trip.start_date)
        self.start_date_entry.config(state= "disabled")

    def __add_save_button(self):
        self.save_button = Button(self.master, text="Save", command=self.__save)
        self.save_button.grid(row=16, column=1)

    def __add_coordinator_label(self):
        self.coordinator_label = Label(self.master)
        self.coordinator_label.grid(row=4, column=0, pady=5, rowspan=3)
        self.coordinator_label.configure(text="Coordinator:")

    def __add_coordinator_entry(self):
        self.coordinator_entry = Listbox(self.master, selectmode="single", exportselection=False)
        self.coordinator_entry.grid(row=4, column=1, pady=5, rowspan=3)
        for user in self.trips_gui.trip_system.users:
            if user.role is RoleTypes.coordinator:
                self.coordinator_entry.insert(END, user.name)
        # for edit view mode
        if self.trip.coordinator is not None:
            for i in range(self.coordinator_entry.size()):
                if self.coordinator_entry.get(i) in self.trip.coordinator.name:
                    self.coordinator_entry.select_set(i)

    def __add_new_coordinator_button(self):
        self.add_new_coordinator_button = Button(self.master, text="Add New", command=self.__open_add_new_coordinator)
        self.add_new_coordinator_button.grid(row=4, column=2)

    def __add_remove_coordinator_button(self):
        self.remove_coordinator_button = Button(self.master, text="Remove Selected",
                                                command=self.__remove_selected_coordinator)
        self.remove_coordinator_button.grid(row=5, column=2)

    def __open_add_new_coordinator(self):
        self.add_new_coordinator_gui = CoordinatorGUI(self)

    def __remove_selected_coordinator(self):
        for i in self.coordinator_entry.curselection():
            self.coordinator_entry.delete(i)
            user = [x for x in self.trips_gui.trip_system.users if self.coordinator_entry.get(i) in x.name][0]
            self.trip.assign_coordinator(None)
            self.trips_gui.trip_system.users.remove(user)

    def __edit_selected_coordinator_button(self):
        self.edit_coordinator_button = Button(self.master, text="Edit Selected", command= self.__open_update_coordinator)
        self.edit_coordinator_button.grid(row=6, column=2)

    def __open_update_coordinator(self):
        if len(self.coordinator_entry.curselection()) <= 0:
            return messagebox.showwarning("Edit Warning", "Please select a element first")

        coordinator = [x for x in self.trips_gui.trip_system.users if
                       self.coordinator_entry.get(self.coordinator_entry.curselection()[0]) in x.name][0]
        self.update_coordinator_gui = CoordinatorGUI(self, coordinator)

    def update_coordinators_info(self):
        self.coordinator_entry.destroy()
        self.__add_coordinator_entry()

    def __add_travellers_label(self):
        self.travellers_label = Label(self.master)
        self.travellers_label.grid(row=8, column=0, pady=5, rowspan=3)
        self.travellers_label.configure(text="Travellers:")

    def __add_travellers_entry(self):
        self.travellers_entry = Listbox(self.master, selectmode="multiple", exportselection=False)
        self.travellers_entry.grid(row=8, column=1, pady=5, rowspan=3)
        for traveller in self.trip.travellers:
            self.travellers_entry.insert(END, traveller.name)

    def __add_new_traveller_button(self):
        self.add_new_traveller_button = Button(self.master, text="Add New", command=self.__open_add_new_traveller)
        self.add_new_traveller_button.grid(row=8, column=2)

    def __remove_selected_traveller_button(self):
        self.remove_selected_traveller_button = Button(self.master, text="Remove Selected",
                                                       command=self.__remove_selected_traveller)
        self.remove_selected_traveller_button.grid(row=9, column=2)

    def __edit_selected_traveller_button(self):
        self.edit_selected_traveller_button = Button(self.master, text="Edit Selected",
                                                     command=self.__remove_selected_traveller)
        self.edit_selected_traveller_button.grid(row=10, column=2)

    def __open_add_new_traveller(self):
        self.add_new_traveller_gui = AddNewTravellerGUI(self)

    def __remove_selected_traveller(self):
        for i in self.travellers_entry.curselection():
            self.travellers_entry.delete(i)
            traveller = [x for x in self.trip.travellers if self.travellers_entry.get(i) in x.name][0]
            self.trip.remove_traveller(traveller.id)

    def __add_trip_legs_label(self):
        self.trip_legs_label = Label(self.master)
        self.trip_legs_label.grid(row=12, column=0, pady=5, rowspan=3)
        self.trip_legs_label.configure(text="Trip Legs:")

    def __add_trip_legs_entry(self):
        self.trip_legs_entry = Listbox(self.master, selectmode="multiple", exportselection=False)
        self.trip_legs_entry.grid(row=12, column=1, pady=5, rowspan=3)
        for trip_leg in self.trip.trip_legs:
            self.trip_legs_entry.insert(END, trip_leg.destination)

    def __add_new_trip_legs_button(self):
        self.add_new_trip_legs_button = Button(self.master, text="Add New", command=self.__open_add_new_trip_leg)
        self.add_new_trip_legs_button.grid(row=12, column=2)

    def __open_add_new_trip_leg(self):
        self.dd_new_trip_leg_gui = AddNewTripLegGUI(self)

    def __remove_selected_trip_legs_button(self):
        self.remove_selected_trip_legs_button = Button(self.master, text="Remove Selected",
                                                       command=self.__remove_selected_trip_leg)
        self.remove_selected_trip_legs_button.grid(row=13, column=2)

    def __edit_selected_trip_legs_button(self):
        self.edit_selected_trip_legs_button = Button(self.master, text="Edit Selected",
                                                       command=self.__remove_selected_trip_leg)
        self.edit_selected_trip_legs_button.grid(row=14, column=2)

    def __remove_selected_trip_leg(self):
        for i in self.trip_legs_entry.curselection():
            self.trip_legs_entry.delete(i)
            trip_legs = [x for x in self.trip.trip_legs if self.trip_legs_entry.get(i) in x.destination][0]
            self.trip.trip_legs.remove(trip_legs)

    def __add_separator(self):
        separator = Separator(self.master, orient='horizontal')
        separator.grid(sticky="ew", columnspan=3)


