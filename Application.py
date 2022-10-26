import csv
import os, sys, subprocess
from openpyxl import Workbook


class Application:
    def __init__(self, filename, typeOfAccess):
        self.filename = filename
        self.typeOfAccess = typeOfAccess
        self.application = Workbook()


    def closeApplication(self):
       self.application.close()


    def showApplication(self):
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, self.filename])

