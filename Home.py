import tkinter as tk
from tkinter import ttk

# Callback functions for directing to desired files
def EPRCallBack():
    import CreateForm_EventPlanning

def RRCallBack():
    import CreateForm_RecruitmentRequest

def CRDCallBack():
    import CreateForm_ClientRequestDetails

def FRCallBack():
    import CreateForm_FinancialRequest

def EFCallBack():
    import EditForm


class HomePage(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Swedish Events Planners")
        self.configure(bg="white")
        # Button for creating new files
        B1 = tk.Button(self, text="Create a new Event Planning Request", command=EPRCallBack)
        B1.grid(row=5, column=1)
        B2 = tk.Button(self, text="Create a new Recruitment Request", command=RRCallBack)
        B2.grid(row=8, column=1)
        B3 = tk.Button(self, text="Create a new Client Request Details form", command=CRDCallBack)
        B3.grid(row=11, column=1)
        B4 = tk.Button(self, text="Create a new Financial Request", command=FRCallBack)
        B4.grid(row=14, column=1)
        # Button to edit existing file
        B5 = tk.Button(self, text="Edit an existing Event Planning Request", command=EFCallBack)
        B5.grid(row=5, column=3)
        B6 = tk.Button(self, text="Edit an existing Recruitment Request", command=EFCallBack)
        B6.grid(row=8, column=3)
        B7 = tk.Button(self, text="Edit an existing Client Request Details form", command=EFCallBack)
        B7.grid(row=11, column=3)
        B8 = tk.Button(self, text="Edit an existing Financial Request", command=EFCallBack)
        B8.grid(row=14, column=3)



if __name__ == "__main__":
    root = HomePage()
    root.mainloop()

