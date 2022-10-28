from tkinter import *

# Create interface
root = Tk()
root.title("Swedish Events Planners")

# Callback functions for directing to desired files
def EPRCallBack():
   import CreateForm_EventPlanning

def RRCallBack():
   import CreateForm_RecruitmentRequest

def CRDCallBack():
   import CreateForm_ClientRequestDetails

def FRCallBack():
   import CreateForm_FinancialRequest

# Button Setting
B1 = Button(root, text ="Create a new Event Planning Request", command = EPRCallBack)
B1.grid(row = 0, column = 1)
B1.pack()

B2 = Button(root, text ="Create a new Recruitment Request", command = RRCallBack)
B2.grid(row = 2, column = 1)
B2.pack()

B3 = Button(root, text ="Create a new Client Request Details form", command = CRDCallBack)
B3.grid(row = 4, column = 1)
B3.pack()

B4 = Button(root, text ="Create a new Financial Request", command = FRCallBack)
B4.grid(row = 6, column = 1)
B4.pack()


root.mainloop()