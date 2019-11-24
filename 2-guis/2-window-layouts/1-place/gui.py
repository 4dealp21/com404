from tkinter import *

class Gui(Tk):

  # initialise window
    def __init__(self):
        super().__init__()

        # set window attributes
        self.title("Newsteller")
        self.configure(bg="#ccc",
                       height=200,
                       width=360)

        
        self.add_outter_box()
        self.add_heading_label()
        self.add_mid_label()
        self.add_email_label()
        self.add_entry_box()
        self.add_button()

    def add_outter_box(self):
        self.outter_box = Frame()
        self.outter_box.place(x=10, y=10, relheight=0.84, relwidth=0.94)

    def add_heading_label(self):
        self.heading_label = Label(self.outter_box)
        self.heading_label.place(x=20, y=20)
        self.heading_label.configure(bg="#eee",
                                     justify=LEFT,
                                     padx=10,
                                     font="Arial 16",
                                     text="RECEIVE OUR NEWLETTER")

    def add_mid_label(self):
        self.mid_label = Label(self.outter_box)
        self.mid_label.place(x=20, y=45)
        self.mid_label.configure(bg="#eee",
                                 justify=LEFT,
                                 pady=20,
                                 text="Please enter your email bellow to recieve our newsletter")

    def add_email_label(self):
        self.email_label = Label(self.outter_box)
        self.email_label.place(x=20, y=80)
        self.email_label.configure(bg="#eee",
                                   justify=LEFT,
                                   pady=20,
                                   text="Email:")

    def add_entry_box(self):
        self.entry_box = Entry(self.outter_box)
        self.entry_box.place(x=70, y=100)
        self.entry_box.configure(width=40)

    def add_button(self):
        self.button = Button(self.outter_box)
        self.button.place(x=0, y=140)
        self.button.configure(bg="#fcc",
                              text="Subscribe",
                              width=47)
