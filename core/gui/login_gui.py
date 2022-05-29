from tkinter import Label, Button
from tkinter import messagebox
from tkinter.ttk import Entry


class LoginGUI():

    def __init__(self, master, trip_system):
        self.trip_system = trip_system
        self.master = master
        self.__add_username_label()
        self.__add_username_entry()
        self.__add_password_label()
        self.__add_password_entry()
        self.__add_login_button()

    def __login(self):
        try:
            if not self.username_entry.get() or not self.password_entry.get():
                messagebox.showerror("Login Failed", "Please enter a valid data")
            else:
                self.trip_system.logging_in(self.username_entry.get(), self.password_entry.get())
        except:
            messagebox.showerror("Login Failed", "You enter a wrong credentials")

    def __add_username_label(self):
        self.username_label = Label()
        self.username_label.grid(row=0, column=0, pady=5)
        self.username_label.configure(text="User name")

    def __add_username_entry(self):
        self.username_entry = Entry()
        self.username_entry.grid(row=0, column=1)

    def __add_password_label(self):
        self.password_label = Label()
        self.password_label.grid(row=1, column=0, pady=5)
        self.password_label.configure(text="Password")

    def __add_password_entry(self):
        self.password_entry = Entry()
        self.password_entry.grid(row=1, column=1)

    def __add_login_button(self):
        self.login_button = Button()
        self.login_button.grid(row=2, column=1, pady=5)
        self.login_button.configure(command=self.__login, text="Login")

    def __del__(self):
        for widgets in self.master.winfo_children():
            widgets.destroy()
