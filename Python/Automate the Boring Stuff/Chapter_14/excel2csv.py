#!python
#excel2csv.py - converts all the Excel files in the current working directory into a CSV file

import csv, openpyxl, os

print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')

for excelFile in os.listdir('.'):
    #skip non-xslx files, load the workbook object
    for sheetName in wb.get_sheet_names():
