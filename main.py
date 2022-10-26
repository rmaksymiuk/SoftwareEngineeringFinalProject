from Application import Application
from Database import Database

newApp = Application('Applications/application.xlsx', 'whatever ')
newApp.showApplication()

database = Database()
database.loadDatabase()
database.showDatabase()

