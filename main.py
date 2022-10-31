from Application import Application
from Database import Database
import xlsxwriter as xls
import pandas as pd

#newApp = Application('Applications/application.xlsx', 'whatever ')
#newApp.showApplication()
# key = 'hi'
# data = {'hi': [1,2,3], 'bye': ['1','2','3']}
#
#
# first = data.get('hi')[0]
# print(first)
database = Database()
database.loadDatabase()
database.loadPermissions()
database.showDatabase()

# path = 'Applications/test.xlsx'
# workbook = xls.Workbook(path)
# worksheet = workbook.add_worksheet()
# worksheet.write(0,0, "haha")
# workbook.close()

