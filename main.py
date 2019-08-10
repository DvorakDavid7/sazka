import time
import openpyxl
from searching import Searching
from prepare_data import Prepare_data
from control_panel import Control_panel
from searchingJ import Searching_Jirka

from tkinter import filedialog
from tkinter.filedialog import askdirectory
import time

class Finder(Searching, Prepare_data, Control_panel, Searching_Jirka):
    def __init__(self):
        with open("memory.txt", "r") as memory:
            pom = memory.readlines()
            self.database_path = pom[0].replace("\n", "")

        self.database = list(open(self.database_path, "r"))

        self.excel_path = "G:\\serial numbers\\new\\Zentiva_EU_Alerts_20190714.xlsx"
        self.book = openpyxl.load_workbook(self.excel_path)
        self.sheet = self.book.active
        self.colourFill = openpyxl.styles.PatternFill(start_color="00b0f0", end_color="00b0f0",fill_type='solid')

        Control_panel.__init__(self)

    def finding_binary_search(self):
        start = time.time()
        counter = 0
        for i in range(len(self.sheet["Q"])):
            cell = str(self.sheet.cell(row=i + 2, column=17).value).upper().replace("Z", "Y") + "\n"
            if self.search(cell, self.database):
                counter += 1
        self.text_counter.set("counter: " + str(counter))
        self.text_time.set("time: " + str(time.time() - start))

    def finding_jirka(self):
        self.label_stat.grid(row = 1, column = 0, sticky = "W")
        self.text_stat.set("In Progress")
        save = filedialog.asksaveasfilename(initialdir = "/",title = "Save as",filetypes = (("xlsx files","*.xlsx"),("all files","*.*")))
        arrExcel = []
        for i in range(len(self.sheet["Q"])):
            cell = str(self.sheet.cell(row=i + 2, column=17).value).upper().replace("Z", "Y") + "\n"
            arrExcel.append(cell)
        arrExcel.sort()
        nums = self.finder_jirka(arrExcel, self.database)

        for i in range(len(self.sheet["Q"])):
            cell = str(self.sheet.cell(row=i + 2, column=17).value).upper().replace("Z", "Y") + "\n"
            if cell in nums:
                self.sheet.cell(row=i + 2, column=17).fill = self.colourFill

        self.text_stat.set("Done")
        self.book.save(save)

    def number_of_matches(self):
        start = time.time()
        arrExcel = []
        for i in range(len(self.sheet["Q"])):
            cell = str(self.sheet.cell(row=i + 2, column=17).value).upper().replace("Z", "Y") + "\n"
            arrExcel.append(cell)
        arrExcel.sort()
        counter = len(self.finder_jirka(arrExcel, self.database))

        self.label_time.grid(row = 1, column = 0, sticky = "W")
        self.label_counter.grid(row = 2, column = 0, sticky = "W")
        self.text_counter.set("matches: " + str(counter) )
        self.text_time.set("time: " + str(time.time() - start) + " sec")

    def create_database(self):  # nahrát txt ---> uložit seřazené txt
        self.label_stat.grid(row = 1, column = 0, sticky = "W")
        self.text_stat.set("In Progress")

        database_path = filedialog.askopenfilename(initialdir = "/",title = "Select database",filetypes = (("txt files","*.txt"),("all files","*.*")))
        save = filedialog.asksaveasfilename(initialdir = "/",title = "Save as",filetypes = (("txt files","*.txt"),("all files","*.*")))

        self.prepare(database_path, save)

        with open("memory.txt", "w") as memory:
            memory.write(save)
        with open("memory.txt", "r") as memory:
            pom = memory.readlines()
            self.database_path = pom[0].replace("\n", "")
            self.database = list(open(self.database_path, "r"))

        self.text_path.set("database: \n" + self.database_path)
        self.text_stat.set("Done")



def main():
    x = Finder()

main()
