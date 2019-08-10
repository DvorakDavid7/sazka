import time
import openpyxl
from searching import Searching
from prepare_data import Prepare_data
from control_panel import Control_panel
from searchingJ import Searching_Jirka


class Finder(Searching, Prepare_data, Control_panel, Searching_Jirka):
    def __init__(self):
        self.database_path = "C:\\Users\\David\\Desktop\\sazka\\sazka\\database\\sorted_data.txt"
        self.excel_path = "G:\\serial numbers\\new\\Zentiva_EU_Alerts_20190714.xlsx"

        self.database = list(open(self.database_path, "r"))

        self.book = openpyxl.load_workbook(self.excel_path)
        self.sheet = self.book.active
        Control_panel.__init__(self)

    def binary_search(self):
        start = time.time()
        counter = 0
        for i in range(len(self.sheet["Q"])):
            cell = str(self.sheet.cell(row=i + 2, column=17).value).upper().replace("Z", "Y") + "\n"
            if self.search(cell, self.database):
                counter += 1
        self.text_counter.set("counter: " + str(counter))
        self.text_time.set("time: " + str(time.time() - start))

    def jirka(self):
        start = time.time()
        arrExcel = []
        for i in range(len(self.sheet["Q"])):
            cell = str(self.sheet.cell(row=i + 2, column=17).value).upper().replace("Z", "Y") + "\n"
            arrExcel.append(cell)
        arrExcel.sort()

        counter = self.searching_jirka(arrExcel, self.database)

        self.text_counter.set("counter: " + str(counter))
        self.text_time.set("time: " + str(time.time() - start))



def main():
    x = Finder()

main()
