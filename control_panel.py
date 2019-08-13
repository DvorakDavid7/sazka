from tkinter import *


class Control_panel:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("500x500")
        self.root.title("Control Panel")

        self.text_field = Frame(self.root)
        self.buttons = Frame(self.root)

        self.text_time = StringVar()
        self.text_counter = StringVar()
        self.text_stat = StringVar()
        self.text_path = StringVar()


        self.label_stat = Label(self.text_field, textvariable = self.text_stat, font = "Helvetica 12")
        self.label_time = Label(self.text_field, textvariable = self.text_time, font = "Helvetica 12")
        self.label_counter = Label(self.text_field, textvariable = self.text_counter, font = "Helvetica 12")
        self.label_current_database = Label(self.text_field, textvariable = self.text_path, font = "Helvetica 9")
        self.text_path.set("database: \n" + self.database_path)

        b2 = Button(self.buttons,width = 26,height = 5,padx = 4, text="number of matches",font="Helvetica 12", command = lambda:(self.ungrid(), self.number_of_matches()))
        b1 = Button(self.buttons,width = 26,height = 5,padx = 4, text="Create database",font="Helvetica 12", command = lambda:(self.ungrid(), self.create_database()))
        b3 = Button(self.buttons,width = 26,height = 5,padx = 4, text="Run Finder",font="Helvetica 12", command = lambda:(self.ungrid(), self.finding_jirka()))
        b4 = Button(self.buttons,width = 26,height = 5,padx = 4, text="Detector",font="Helvetica 12", command = lambda:(self.ungrid(), self.detector()))
        b5 = Button(self.buttons,width = 26,height = 5,padx = 4, text="Insert into database",font="Helvetica 12", command = lambda:(self.ungrid(), self.insert_into_database()))
        b6 = Button(self.buttons,width = 26,height = 5,padx = 4, text="mistakes detector",font="Helvetica 12", command = lambda:(self.ungrid(), self.mistakes_detector()))


        b1.grid(row = 0, column = 0)
        b2.grid(row = 0, column = 1)
        b3.grid(row = 1, column = 0)
        b4.grid(row = 1, column = 1)
        b5.grid(row = 2, column = 0)
        b6.grid(row = 2, column = 1)

        self.text_field.grid(row=0,column=0)
        self.buttons.grid(row=1,column=0)

        self.label_current_database.grid(row = 0, column = 0)


        mainloop()


    def ungrid(self):
        self.label_stat.grid_forget()
        self.label_time.grid_forget()
        self.label_counter.grid_forget()
