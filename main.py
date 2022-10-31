from Application import Application
from Database import Database
import xlsxwriter as xls
import pandas as pd

#newApp = Application('Applications/application.xlsx', 'whatever ')
#newApp.showApplication()
current_users =  {'Bob123': ['123qwe', 'Service Manager', ['rw', 'r', 'r', 'r']]}
                  # 'Jonh222': ['123qwe', 'Production Manager', ['rw', 'r', 'r', 'r']],
                  # 'Alex456': ['123qwe', 'SubTeam', ['rw', 'r', 'r', 'r']],
                  # 'Draymond333': ['123qwe', 'Administrator', ['rw', 'r', 'r', 'r']]}

database = Database(current_users)
database.writeUsersToExcel()
#database.loadDatabase()
database.showDatabase()

# path = 'Applications/test.xlsx'
# workbook = xls.Workbook(path)
# worksheet = workbook.add_worksheet()
# worksheet.write(0,0, "haha")
# workbook.close()

for col in range(4):
    print(col)
