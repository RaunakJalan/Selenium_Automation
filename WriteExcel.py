import openpyxl

path = "D:\certificates\Selenium\write_test.xlsx"

workbook = openpyxl.load_workbook(path)

sheet = workbook.active #workbook.get_sheet_by_name("Sheet name")


for r in range(1,6):
    for c in range(1,4):
        sheet.cell(row=r, column=c).value="welcome"

workbook.save(path)
