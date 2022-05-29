from tkinter import Toplevel, Label, Entry, Button, END

from core.models.traveller import Traveller


class AddNewTravellerGUI:
    def __init__(self, trip_gui):
        self.trip_gui = trip_gui
        self.new_traveller = Traveller(None, None, None, None, [], [], [])
        self.master = Toplevel()
        self.master.title("Add a Traveller")
        self.__add_name_label()
        self.__add_name_entry()
        self.__add_address_label()
        self.__add_address_entry()
        self.__add_save_button()

    def __save(self):
        # save
        self.new_traveller.name = self.name_entry.get()
        self.new_traveller.address = self.address_entry.get()

        self.trip_gui.trip.travellers.append(self.new_traveller)
        self.trip_gui.travellers_entry.insert(END, self.new_traveller.name)
        self.master.destroy()

    def __add_name_label(self):
        self.name_label = Label(self.master)
        self.name_label.grid(row=0, column=0, pady=5)
        self.name_label.configure(text="Name:")

    def __add_name_entry(self):
        self.name_entry = Entry(self.master)
        self.name_entry.grid(row=0, column=1, pady=5)

    def __add_address_label(self):
        self.address_label = Label(self.master)
        self.address_label.grid(row=1, column=0, pady=5)
        self.address_label.configure(text="address:")

    def __add_address_entry(self):
        self.address_entry = Entry(self.master)
        self.address_entry.grid(row=1, column=1)

    def __add_save_button(self):
        self.save_button = Button(self.master, text="Save", command=self.__save)
        self.save_button.grid(row=6, column=1)

    # todo need to add the other fields
    # todo should add a validtaion to the input also name should be a unique