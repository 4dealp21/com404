#import tkinter

from tkinter import *
from tkinter import messagebox

class TCA(Tk):

    def __init__(self):
        super().__init__()

        self.field_image = PhotoImage(file="default.gif")
        self.field_image_green = PhotoImage(file="filled.gif")
        self.field_image_red = PhotoImage(file="empty.gif")

        #set window propreties
        self.title("Newsletter")
        self.configure(bg="#ccc", padx=10, pady=10)

        self.add_outer_frame()
        self.add_heading_label()
        self.add_instruction_label()
        self.add_email_label()
        self.add_email_entry()
        self.add_field_image_label()
        self.add_subscribe_button()

    def add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=0)
        self.outer_frame.configure(bg="#eee")
    
    def add_heading_label(self):
        self.heading_label=Label(self.outer_frame)
        self.heading_label.grid(row=0, column=0, columnspan=2)
        self.heading_label.configure(text="RECEIVE OUR NEWSLETTER", font="Arial 14", pady=10)

    def add_instruction_label(self):
        self.instruction_label=Label(self.outer_frame)
        self.instruction_label.grid(row=1, column=0, columnspan=2, sticky=W)
        self.instruction_label.configure(text="Please enter your email bellow to receive our newsletter.", pady=10, padx=10)

    def add_email_label(self):
        self.email_label=Label(self.outer_frame)
        self.email_label.grid(row=2, column=0, sticky=W)
        self.email_label.configure(text="Email:", padx=15, pady=10)

    def add_email_entry(self):
        self.email_entry=Entry(self.outer_frame)
        self.email_entry.grid(row=2, column=0, sticky=E, padx=10)
        self.email_entry.configure(width=30, fg="#f00")

        self.email_entry.bind("<KeyRelease>", self.image_switch)

    def add_field_image_label(self):
        self.field_image_label=Label(self.outer_frame)
        self.field_image_label.grid(row=2, column=1, sticky=W)
        self.field_image_label.configure(image=self.field_image)

    def add_subscribe_button(self):
        self.subscribe_button=Button(self.outer_frame)
        self.subscribe_button.grid(row=3, column=0, columnspan=2, sticky=N+W+S+E)
        self.subscribe_button.configure(bg="#fee", text="Subscribe")

        self.subscribe_button.bind("<ButtonRelease-1>", self.subscribe_button_clicked)

    def image_switch(self, event):
        if (len(self.email_entry.get()) > 0):
            self.field_image_label.configure(image=self.field_image_green)

        else:
            self.field_image_label.configure(image=self.field_image_red)

    def subscribe_button_clicked(self, event):
        messagebox.showinfo("Newsletter", "Susbcribed!")


if __name__ == "__main__":
    my_gui = TCA()
    my_gui.mainloop()
        