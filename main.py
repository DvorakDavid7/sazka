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
            self.database_path = pom[0]
        self.database = list(open(self.database_path, "r"))
        Control_panel.__init__(self)

    def finding_binary_search(self):
        start = time.time()
        counter = 0
        self.load_excel()
        for i in range(len(self.sheet["Q"])):
            cell = str(self.sheet.cell(row=i + 2, column=17).value).upper().replace("Z", "Y") + "\n"
            if self.search(cell, self.database):
                counter += 1
        self.text_counter.set("counter: " + str(counter))
        self.text_time.set("time: " + str(time.time() - start))

    def finding_jirka(self):
        self.label_stat.grid(row = 1, column = 0, sticky = "W")
        self.text_stat.set("In Progress")
        self.load_excel()
        arrExcel = []
        for i in range(len(self.sheet["Q"])):
            cell = str(self.sheet.cell(row=i + 2, column=17).value).upper().replace("Z", "Y") + "\n"
            arrExcel.append(cell)
        arrExcel.sort()
        nums = self.finder_jirka(arrExcel, self.database)
        # coloring
        for i in range(len(self.sheet["Q"])):
            cell = str(self.sheet.cell(row=i + 2, column=17).value).upper().replace("Z", "Y") + "\n"
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

    def detector(self):
        sn_s =[".",",",";","ů","(",")","@","&","!","^","~","$","%","*","+","´","ˇ","â","¬","¢","Ð","š","º","ª","¦","Ÿ","•","Ñ","€","¶","¥","’","™","—","£"]
        with open("special_characters\\SN-ZTVForbid.txt", "r") as f:
            SN_ZTVForbid = f.read().splitlines()

        self.label_stat.grid(row = 1, column = 0, sticky = "W")
        self.text_stat.set("In Progress")
        self.load_excel()

        for i in range(len(self.sheet["Q"]) - 1):
            cell = str(self.sheet.cell(row=i + 2, column=17).value)
            for l in cell:
                if l in sn_s:
                    self.sheet.cell(row=i + 2, column=26).value = "SN-S"
                elif l in SN_ZTVForbid:
                    self.sheet.cell(row=i + 2, column=27).value = "SN-ZTVForbid"
            if len(cell) != 14:
                self.sheet.cell(row=i + 2, column=28).value = "len: {}".format(len(cell))


        self.book.save(self.excel_path)
        self.text_stat.set("Done")

def main():
    x = Finder()

main()
