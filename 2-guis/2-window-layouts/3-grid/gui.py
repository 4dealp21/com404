from tkinter import *

class Gui(Tk):

  # initialise window
    def __init__(self):
        super().__init__()

        # set window attributes
        self.title("Newsteller")
        self.configure(bg="#ccc", padx=10, pady=10)

        
        self.add_outter_box()
        self.add_heading_label()
        self.add_mid_label()
        self.add_email_label()
        self.add_entry_box()
        self.add_button()

    def add_outter_box(self):
        self.outter_box = Frame()
        self.outter_box.grid(row=0, column=0)
        self.outter_box.configure(bg="#eee", padx=10, pady=10)

    def add_heading_label(self):
        self.heading_label = Label(self.outter_box)
        self.heading_label.grid(row=0, column=0, columnspan=2)
        self.heading_label.configure(bg="#eee",
                                     font="Arial 18",
                                     text="RECEIVE OUR NEWLETTER")

    def add_mid_label(self):
        self.mid_label = Label(self.outter_box)
        self.mid_label.grid(row=1, column=0, columnspan=2, sticky=W)
        self.mid_label.configure(bg="#eee",
                                 padx=10,
                                 text="Please enter your email bellow to recieve our newsletter")

    def add_email_label(self):
        self.email_label = Label(self.outter_box)
        self.email_label.grid(row=2, column=0, sticky=E)
        self.email_label.configure(pady=20,
                                   text="Email:")

    def add_entry_box(self):
        self.entry_box = Entry(self.outter_box)
        self.entry_box.grid(row=2, column=1, sticky=W)
        self.entry_box.configure(width=40)

    def add_button(self):
        self.button = Button(self.outter_box)
        self.button.grid(row=3, column=0, columnspan=2, sticky=N+E+S+W)
        self.button.configure(bg="#fcc",
                              text="Subscribe")
