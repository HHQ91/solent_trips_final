from tkinter import Toplevel, Label, Entry, Button, END, messagebox

from core.models.user import User
from core.types.role_types import RoleTypes


class CoordinatorGUI:
    def __init__(self, trip_gui, coordinator=None):
        self.trip_gui = trip_gui
        if coordinator is not None:
            self.mode = "Edit"
            self.coordinator = coordinator
        else:
            self.mode = "Add"
            self.coordinator = User(None, None, RoleTypes.coordinator)

        self.master = Toplevel()
        self.master.title(f"{self.mode} a coordinator")
        self.__add_name_label()
        self.__add_name_entry()
        self.__add_password_label()
        self.__add_password_entry()
        self.__add_save_button()

    def __save(self):
        # save
        self.coordinator.name = self.name_entry.get()
        if not self.coordinator.name:
            return messagebox.showerror("Add Failed", "please enter a valid name")

        self.coordinator.password = self.password_entry.get()
        if not self.coordinator.password:
            return messagebox.showerror("Add Failed", "please enter a valid password")

        if self.mode == "Edit":
            for i, user in enumerate(self.trip_gui.trips_gui.trip_system.users):
                if user.id == self.coordinator.id:
                    self.trip_gui.trips_gui.trip_system.users[i].name = self.coordinator.name
                    self.trip_gui.trips_gui.trip_system.users[i].password = self.coordinator.password
                    self.trip_gui.update_coordinators_info()
        else:
            self.trip_gui.trips_gui.trip_system.users.append(self.coordinator)
            self.trip_gui.coordinator_entry.insert(END, self.coordinator.name)
        self.master.destroy()

    def __add_name_label(self):
        self.name_label = Label(self.master)
        self.name_label.grid(row=0, column=0, pady=5)
        self.name_label.configure(text="Name:")

    def __add_name_entry(self):
        self.name_entry = Entry(self.master)
        self.name_entry.grid(row=0, column=1, pady=5)
        # for edit view mode
        if self.coordinator.name is not None:
            self.name_entry.insert(0, self.coordinator.name)

    def __add_password_label(self):
        self.password_label = Label(self.master)
        self.password_label.grid(row=1, column=0, pady=5)
        self.password_label.configure(text="Password:")

    def __add_password_entry(self):
        self.password_entry = Entry(self.master)
        self.password_entry.grid(row=1, column=1)
        # for edit view mode
        if self.coordinator.password is not None:
            self.password_entry.insert(0, self.coordinator.password)

    def __add_save_button(self):
        self.save_button = Button(self.master, text="Save", command=self.__save)
        self.save_button.grid(row=6, column=1)

    # todo need to add the other fields
    # todo implement validation
