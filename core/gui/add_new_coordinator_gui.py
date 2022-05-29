from tkinter import Toplevel, Label, Entry, Button, END

from core.models.user import User
from core.types.role_types import RoleTypes


class AddNewCoordinatorGUI:
    def __init__(self, trip_gui):
        self.trip_gui = trip_gui
        self.new_coordinator = User(None, None, RoleTypes.coordinator)
        self.master = Toplevel()
        self.master.title("Add a coordinator")
        self.__add_name_label()
        self.__add_name_entry()
        self.__add_password_label()
        self.__add_password_entry()
        self.__add_save_button()

    def __save(self):
        # save
        self.new_coordinator.name = self.name_entry.get()
        self.new_coordinator.password = self.password_entry.get()

        self.trip_gui.trips_gui.trip_system.users.append(self.new_coordinator)
        self.trip_gui.coordinator_entry.insert(END, self.new_coordinator.name)
        self.master.destroy()

    def __add_name_label(self):
        self.name_label = Label(self.master)
        self.name_label.grid(row=0, column=0, pady=5)
        self.name_label.configure(text="Name:")

    def __add_name_entry(self):
        self.name_entry = Entry(self.master)
        self.name_entry.grid(row=0, column=1, pady=5)

    def __add_password_label(self):
        self.password_label = Label(self.master)
        self.password_label.grid(row=1, column=0, pady=5)
        self.password_label.configure(text="Password:")

    def __add_password_entry(self):
        self.password_entry = Entry(self.master)
        self.password_entry.grid(row=1, column=1)

    def __add_save_button(self):
        self.save_button = Button(self.master, text="Save", command=self.__save)
        self.save_button.grid(row=6, column=1)

    # todo need to add the other fields
    # todo implement validation
