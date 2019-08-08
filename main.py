import time
import openpyxl
from searching import Searching
from prepare_data import Prepare_data

class Finder(Searching, Prepare_data):
    def __init__(self):
        self.database_path = "C:\\Users\\David\\Desktop\\sazka\\database\\sorted_data.txt"
        self.excel_path = "F:\\serial numbers\\new\\Zentiva_EU_Alerts_20190716.xlsx"

        self.database = list(open(self.database_path, "r"))

        self.book = openpyxl.load_workbook(self.excel_path)
        self.sheet = self.book.active

    def find(self):
        counter = 0
        for i in range(len(self.sheet["Q"])):
            cell = str(self.sheet.cell(row=i + 2, column=17).value).upper().replace("Z", "Y") + "\n"
            if self.search(cell, self.database):
                counter += 1

        print("counter: {}".format(counter))


def main():
    if __name__ == "__main__":
        start = time.time()
        x = Finder()
        x.find()
        print((time.time() - start) / 60)
main()
