import time
import openpyxl
from searching import Searching
from prepare_database import Prepare_database
from control_panel import Control_panel
from searchingJ import Searching_Jirka
from prepare_excel import Prepare_excel
from tkinter import filedialog
from tkinter.filedialog import askdirectory
import time


class Finder(Searching, Prepare_database, Control_panel, Searching_Jirka, Prepare_excel):
    def __init__(self):
        with open("memory.txt", "r") as memory:
            pom = memory.read().splitlines()
            if len(pom) == 0:
                self.database_path = "Press Create database"
            else:
                self.database_path = pom[0]
                self.database = list(open(self.database_path, "r"))
        Control_panel.__init__(self)

    def counter_binary_search(self):
        start = time.time()
        counter = 0
        self.load_excel()
        for i in range(len(self.sheet["R"])):
            cell = str(self.sheet.cell(row=i + 2, column=18).value).upper().replace("Z", "Y") + "\n"
            if self.search(cell, self.database):
                counter += 1
        self.text_counter.set("counter: " + str(counter))
        self.text_time.set("time: " + str(time.time() - start))

    def finding_jirka(self):
        self.label_stat.grid(row = 1, column = 0, sticky = "W")
        self.text_stat.set("In Progress")
        self.load_excel()
        arrExcel = []
        for i in range(len(self.sheet["R"])):
            cell = str(self.sheet.cell(row=i + 2, column=18).value).upper().replace("Z", "Y") + "\n"
            arrExcel.append(cell)
        arrExcel.sort()
        nums = self.finder_jirka(arrExcel, self.database)
        # coloring
        for i in range(len(self.sheet["R"])):
            cell = str(self.sheet.cell(row=i + 2, column=18).value).upper().replace("Z", "Y") + "\n"
            if cell in nums:
                self.sheet.cell(row=i + 2, column=17).fill = self.colourFill

        self.text_stat.set("Done")
        self.book.save(self.excel_path)

    def number_of_matches(self):
        self.label_stat.grid(row = 1, column = 0, sticky = "W")
        self.text_stat.set("In Progress")
        self.load_excel()
        start = time.time()
        arrExcel = []
        for i in range(len(self.sheet["R"])):
            cell = str(self.sheet.cell(row=i + 2, column=18).value).upper().replace("Z", "Y") + "\n"
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

    def detector(self):
        sn_s = ".,;ů()@&!^~$%*+´ˇâ¬¢Ðšºª¦Ÿ•Ñ€¶¥’™—£/'[]{}"
        print(len(sn_s))

        self.label_stat.grid(row = 1, column = 0, sticky = "W")
        self.label_time.grid(row = 2, column = 0, sticky = "W")
        self.text_stat.set("In Progress")
        self.text_time.set("")

        self.load_excel()

        start = time.time()
        for i in range(len(self.sheet["R"]) - 1):
            message = ""
            cell = str(self.sheet.cell(row=i + 2, column=18).value)
            for l in cell:
                if l in sn_s:
                    message += "SN-S "
                    break
            if "o" in cell or "O" in cell:
                message += "SN-O "
            if "z" in cell or "Z" in cell:
                message += "SN-YZ "
            if len(cell) == 16 and str(cell[0]) == "2" and str(cell[1]) == "1":
                message += "SN-21 "
            if len(cell) != 14:
                message += "SN-L({}) ".format(len(cell))
            if cell.upper() != cell:
                 message += "SN-LC "
            self.sheet.cell(row=i + 2, column=28).value = message

        self.book.save(self.excel_path)
        self.text_stat.set("Done")
        self.text_time.set("time: " + str(time.time() - start) + " sec")

    def insert_into_database(self):
        self.label_stat.grid(row = 1, column = 0, sticky = "W")
        self.text_stat.set("In Progress")

        new_data_path = filedialog.askopenfilename(initialdir = "/",title = "Select database",filetypes = (("txt files","*.txt"),("all files","*.*")))
        with open(new_data_path, "r") as f:
            new_data = list(f)

        with open(self.database_path, "a") as current_database:
            for text in new_data:
                current_database.write(text)
            current_database.write("\n")

        self.prepare(self.database_path, self.database_path)

        self.text_stat.set("Done")


def main():
    x = Finder()

main()
