from tkinter import Toplevel, Label, Entry, Button, END

from core.models.trip_leg import TripLeg


class AddNewTripLegGUI:
    def __init__(self, trip_gui):
        self.trip_gui = trip_gui
        self.new_trip_leg = TripLeg(None, None, None)
        self.master = Toplevel()
        self.master.title("Add a trip Leg")
        self.__add_start_location_label()
        self.__add_start_location_entry()
        self.__add_destination_label()
        self.__add_destination_entry()
        self.__add_save_button()

    def __save(self):
        # save
        self.new_trip_leg.start_location = self.start_location_entry.get()
        self.new_trip_leg.destination = self.destination_entry.get()

        self.trip_gui.trip.trip_legs.append(self.new_trip_leg)
        self.trip_gui.trip_legs_entry.insert(END, self.new_trip_leg.destination)
        self.master.destroy()

    def __add_start_location_label(self):
        self.start_location_label = Label(self.master)
        self.start_location_label.grid(row=0, column=0, pady=5)
        self.start_location_label.configure(text="Start Location:")

    def __add_start_location_entry(self):
        self.start_location_entry = Entry(self.master)
        self.start_location_entry.grid(row=0, column=1, pady=5)

    def __add_destination_label(self):
        self.destination_label = Label(self.master)
        self.destination_label.grid(row=1, column=0, pady=5)
        self.destination_label.configure(text="Destination:")

    def __add_destination_entry(self):
        self.destination_entry = Entry(self.master)
        self.destination_entry.grid(row=1, column=1)

    def __add_save_button(self):
        self.save_button = Button(self.master, text="Save", command=self.__save)
        self.save_button.grid(row=6, column=1)

    # todo need to add the other fields
    # todo should add a validtaion to the input also name should be a unique