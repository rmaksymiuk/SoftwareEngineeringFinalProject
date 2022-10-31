import csv
import os, sys, subprocess
from openpyxl import Workbook, load_workbook


class Application:
    def __init__(self, filename, newFormNum):
        self.filename = filename
        self.newFormNum = newFormNum


    def closeApplication(self):
       self.application.close()


    def showApplication(self, filename):
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])

    #create applications
    def createForm(self, type):
        #possible types of the forms:
        # ClientRequestDetails, FinancialRequest, EventPlanningRequest, RecruitmentRequest
        switcher = {'ClientRequestDetails': 'D3', 'FinancialRequest': 'E3',
                    'EventPlanningRequest': 'B3', 'RecruitmentRequest' : 'C3'}
        wbNumber = load_workbook(self.newFormNum)
        wsNumber = wbNumber.active
        caseNum = wsNumber[switcher.get(type)].value + 1
        wsNumber[switcher.get(type)].value = caseNum
        wbNumber.save(self.newFormNum)

        wb = load_workbook(self.filename)
        ws = wb.active
        ws['A2'].value = caseNum
        print(ws['A2'].value)
        dest_filename = 'Applications/' + type + str(caseNum) + '.xlsx'
        wb.save(dest_filename)
        self.showApplication(dest_filename)

        return



