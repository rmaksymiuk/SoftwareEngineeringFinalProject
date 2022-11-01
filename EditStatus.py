from tkinter import *
import os , sys, subprocess, fnmatch
from Application import Application
from Database import Database


class SearchFileStatus(Tk):
    def __init__(self):
        super().__init__()

        self.title('Search for your case')
        canvas1 = Canvas(self, width=400, height=300)
        canvas1.pack()
        entry1 = Entry(self)
        canvas1.create_window(200, 140, window=entry1)

        def SearchCaseStatus():
            database = Database()
            database.loadDatabase()
            database.loadStatus()
            #Search in database for the status
            InputCaseID = entry1.get()
            InputCase = Application("Applications/FinancialRequest.xlsx", "Applications/NewestFormNumber.xlsx")
            InputCase.filename = InputCaseID
            for element in database.status.keys():
                element = str(element)
                if element == InputCase.filename:
                    element = int(element)
                    InputCase.status = database.status.get(element)

            print(type(InputCase.filename),InputCase.filename, type(InputCase.status), InputCase.status)
            EditCaseStatus(InputCase).mainloop()

        button1 = Button(self, text='Search for the Case ID', command=SearchCaseStatus)
        canvas1.create_window(200, 180, window=button1)

class EditCaseStatus(Tk):
    def __init__(self, InputCase):
        super().__init__()
        database = Database()
        database.loadStatus()
        self.title('Status Update')
        canvas1 = Canvas(self, width=400, height=300)
        canvas1.pack()
        label1 = Label(self, text="Current status:" + InputCase.status)
        canvas1.create_window(200, 140, window=label1)
        print(type(InputCase.filename), InputCase.filename, type(InputCase.status), InputCase.status)
        InputCase.filename = int(InputCase.filename)
        button1 = Button(self, text='Approve', command=lambda: database.changeStatus(InputCase.filename, 'Approved') )
        canvas1.create_window(100, 200, window=button1)

        button2 = Button(self, text='Reject', command=lambda: database.changeStatus(InputCase.filename, 'Rejected'))
        canvas1.create_window(300, 200, window=button2)

if __name__ == "__main__":
    root = SearchFileStatus()
    root.mainloop()