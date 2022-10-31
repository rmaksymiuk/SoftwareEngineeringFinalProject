import tkinter as tk
from tkinter import ttk
from User import User
from Application import Application

# Callback functions for directing to desired files

#Event Planning Request
def EPRCallBack(user):
    #check for permission
    if user.permissions['EventPlanning'] == 'rw':
        #create the application
        application = Application("Applications/EventPlanningRequest.xlsx", "Applications/NewestFormNumber.xlsx")
        application.createForm('EventPlanningRequest')
    else:
        print(f'Sorry the user: {user.username} does not have permission to perform this action.')
        return

#Create a new Recruitment Request
def RRCallBack(user):
    if user.permissions['RecruitmentRequest'] == 'rw':
        #create the application
        application = Application("Applications/RecruitmentRequest.xlsx", "Applications/NewestFormNumber.xlsx")
        application.createForm('RecruitmentRequest')
    else:
        print(f'Sorry the user: {user.username} does not have permission to perform this action.')
        return

#Create a new Client Request Details form
def CRDCallBack(user):
    if user.permissions['ClientRequest'] == 'rw':
        #create the application
        application = Application("Applications/ClientRequestDetails.xlsx", "Applications/NewestFormNumber.xlsx")
        application.createForm('ClientRequestDetails')
    else:
        print(f'Sorry the user: {user.username} does not have permission to perform this action.')
        return

def FRCallBack(user):
    if user.permissions['FinancialRequest'] == 'rw':
        #create the application
        application = Application("Applications/FinancialRequest.xlsx", "Applications/NewestFormNumber.xlsx")
        application.createForm('FinancialRequest')
    else:
        print(f'Sorry the user: {user.username} does not have permission to perform this action.')
        return

def EFCallBack(user):
    import EditForm


class HomePage(tk.Tk):
    def __init__(self, user):
        super().__init__()
        self.user = user

        self.title("Swedish Events Planners")
        self.configure(bg="white")
        # Button for creating new files
        B1 = tk.Button(self, text="Create a new Event Planning Request", command=lambda:EPRCallBack(self.user))
        B1.grid(row=5, column=1)
        B2 = tk.Button(self, text="Create a new Recruitment Request", command=lambda:RRCallBack(self.user))
        B2.grid(row=8, column=1)
        B3 = tk.Button(self, text="Create a new Client Request Details form", command=lambda:CRDCallBack(self.user))
        B3.grid(row=11, column=1)
        B4 = tk.Button(self, text="Create a new Financial Request", command=lambda:FRCallBack(self.user))
        B4.grid(row=14, column=1)


        # Button to edit existing file
        B5 = tk.Button(self, text="Edit an existing Event Planning Request", command=lambda:EFCallBack(self.user))
        B5.grid(row=5, column=3)
        B6 = tk.Button(self, text="Edit an existing Recruitment Request", command=lambda:EFCallBack(self.user))
        B6.grid(row=8, column=3)
        B7 = tk.Button(self, text="Edit an existing Client Request Details form", command=lambda:EFCallBack(self.user))
        B7.grid(row=11, column=3)
        B8 = tk.Button(self, text="Edit an existing Financial Request", command=lambda:EFCallBack(self.user))
        B8.grid(row=14, column=3)



if __name__ == "__main__":
    root = HomePage()
    root.mainloop()

