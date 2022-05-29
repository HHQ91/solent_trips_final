from tkinter import ttk, StringVar, Label, Button, Toplevel
from tkinter.ttk import Entry, Frame, Separator, Combobox
from tkcalendar import DateEntry
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
            Separator(orient='horizontal').pack(fill='x')
            trip_info = f"Trip: {trip.name}, duration: {trip.duration.name}, start in: {trip.start_date}"
            trip_name_label = Label()
            trip_name_label.pack()
            trip_name_label.configure(text=trip_info)
            self.trip_info_widgets.append(trip_name_label)

    def __add_trip_info(self, trip):
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
        self.new_trip_popup_window = Toplevel()
        self.new_trip_popup_window.title("Add a trip")
        # name
        Label(self.new_trip_popup_window, text="Name: ").grid(row=0, column=0, pady=5)
        self.new_trip_name_entry = Entry(self.new_trip_popup_window)
        self.new_trip_name_entry.grid(row=0, column=1)

        # duration
        Label(self.new_trip_popup_window, text="Duration: ").grid(row=1, column=0, pady=5)
        self.new_trip_duration_entry = Combobox(self.new_trip_popup_window, values=(
            DurationTypes.weekend.name, DurationTypes.one_day.name, DurationTypes.fortnight.name))
        self.new_trip_duration_entry.grid(row=1, column=1)

        # start date
        Label(self.new_trip_popup_window, text="Start date: ").grid(row=2, column=0, pady=5)
        self.new_trip_start_date_entry = DateEntry(self.new_trip_popup_window)
        self.new_trip_start_date_entry.grid(row=2, column=1)

        # save button
        self.save_new_trip_button = Button(self.new_trip_popup_window, text="Save", command=self.__save_new_trip)
        self.save_new_trip_button.grid(row=3, column=1)

    def __save_new_trip(self):
        trip = Trip(
            self.new_trip_name_entry.get(),
            self.new_trip_start_date_entry.get(),
            DurationTypes[self.new_trip_duration_entry.get()],
            None, None, None)
        print(trip.duration)
        self.trip_system.trips.append(trip)
        self.__add_trip_info(trip)
        self.new_trip_popup_window.destroy()
