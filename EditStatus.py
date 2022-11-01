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
            for InputCase.filename in database.status:
                InputCase.status = database.status.get(InputCase.filename)
                print(InputCase.filename, InputCase.status)
            EditCaseStatus(InputCase).mainloop()

        button1 = Button(self, text='Search for the Case ID', command=SearchCaseStatus)
        canvas1.create_window(200, 180, window=button1)

class EditCaseStatus(Tk):
    def __init__(self, inputCase):
        super().__init__()

        self.title('Status Update')
        canvas1 = Canvas(self, width=400, height=300)
        canvas1.pack()
        label1 = Label(self, text="Current status:" + inputCase.status)
        canvas1.create_window(200, 140, window=label1)

        button1 = Button(self, text='Approve', command=inputCase.approveApplication)
        canvas1.create_window(100, 200, window=button1)

        button2 = Button(self, text='Reject', command=inputCase.rejectApplication)
        canvas1.create_window(300, 200, window=button2)

if __name__ == "__main__":
    root = SearchFileStatus()
    root.mainloop()