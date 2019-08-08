import time
import openpyxl


data = set(open("D:\\serial numbers\\Data\\result.txt", "r"))
data = list(data)
data.sort()

book = openpyxl.load_workbook("D:\\serial numbers\\Zentiva_EU_Alerts_20190606.xlsx")
sheet = book.active

def data_change():
    sort_data = open("sort_data.txt", "w")

    for i in range(len(data)):
        sort_data.write(data[i])

    sort_data.close()


def search(target,data):
    while len(data) > 0:
        if target < data[0] or target > data[len(data) - 1]:
            return False
        midd = int(len(data) / 2)
        if data[midd] == target:
            return True
        if data[midd] < target:
            data = data[midd + 1:]
        else:
            data = data[:midd]

def coloring():
    counter = 0
    for i in range(len(sheet["Q"])):
        cell = str(sheet.cell(row=i + 1, column=17).value).upper().replace("Z", "Y") + "\n"
        print(cell)
        if search(cell, data):
            counter += 1

    print("counter: {}".format(counter))


start = time.time()
coloring()
print(time.time() - start)
