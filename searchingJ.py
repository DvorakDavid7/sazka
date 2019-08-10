import openpyxl
import time


class Searching_Jirka:
    def searching_jirka(self,arrExcel, arrDatabase):

        soucet = 0
        k = 0
        for i in range(len(arrExcel)):
            for j in range(k, len(arrDatabase)):
                if arrExcel[i] < arrDatabase[j]:
                    k = j + 1
                    break

                elif arrExcel[i] == arrDatabase[j]:
                    soucet = soucet + 1
                    break
        return soucet


if __name__ == "__main__":
    arrDatabase = list(open("C:\\Users\\EX002236\\Desktop\\sazka\\sazka\\database\\sorted_data.txt", "r"))
    book = openpyxl.load_workbook("C:\\Users\\EX002236\\Desktop\\sázka\\bigdata.xlsx")
    sheet = book.active

    arrExcel = []
    for i in range(len(sheet["Q"])):
        cell = str(sheet.cell(row=i + 2, column=17).value).upper().replace("Z", "Y") + "\n"
        arrExcel.append(cell)
    arrExcel.sort()
