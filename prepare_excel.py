import openpyxl
from tkinter import filedialog
from tkinter.filedialog import askdirectory

class Prepare_excel:
    def load_excel(self):
        self.excel_path = filedialog.askopenfilename(initialdir = "/",title = "Select Excel file",filetypes = (("xlsx files","*.xlsx"),("all files","*.*")))
        self.book = openpyxl.load_workbook(self.excel_path)
        self.sheet = self.book.active
        self.colourFill = openpyxl.styles.PatternFill(start_color="00b0f0", end_color="00b0f0",fill_type='solid')
