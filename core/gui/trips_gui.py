from tkinter import ttk, StringVar, Label, Button
from tkinter.ttk import Entry


class TripsGUI():

    def __init__(self, master, trip_system):
        self.trip_system = trip_system
        self.master = master
        self.__add_label()


    def __add_label(self):
        self.username_label = Label()
        self.username_label.grid(row=0, column=0, pady=5)
        self.username_label.configure(text="Trips")
