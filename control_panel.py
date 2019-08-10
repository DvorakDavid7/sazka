from tkinter import *



class Control_panel:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("500x500")
        self.root.title("Control Panel")

        self.text_field = Frame(self.root)
        self.buttons = Frame(self.root)

        self.text_field.grid(row = 0, column = 0)
        self.buttons.grid(row = 1, column = 0)

        self.text_time = StringVar()
        self.text_counter = StringVar()


        text_time = Label(self.text_field, textvariable = self.text_time, font = "Helvetica 12")
        text_counter = Label(self.text_field, textvariable = self.text_counter, font = "Helvetica 12")
        b1 = Button(self.buttons, text="Půlící algoritmus",font="Helvetica 12", command = self.binary_search)
        b2 = Button(self.buttons, text="Jirkův algoritmus",font="Helvetica 12", command = self.jirka)

        text_time.grid(row = 0, column = 0, sticky = "W")
        text_counter.grid(row = 1, column = 0, sticky = "W")
        b1.grid(row = 0, column = 0, sticky = "W")
        b2.grid(row = 0, column = 1, sticky = "W")

        mainloop()
