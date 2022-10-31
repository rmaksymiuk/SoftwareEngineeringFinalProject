from tkinter import *
import os , sys, subprocess, fnmatch

# Create Interface for
root = Tk()
root.title('Search for your form')
canvas1 = Canvas(root, width=400, height=300)
canvas1.pack()
entry1 = Entry(root)
canvas1.create_window(200, 140, window=entry1)

def GetCaseID():
    InputCaseID = entry1.get()
    for file in os.listdir('Applications/'):
        if fnmatch.fnmatch(file, '*' + str(InputCaseID) + '.xlsx'):
            print(file)
            file = 'Applications/' + file
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, file])


button1 = Button(text='Search for the Case ID', command=GetCaseID)
canvas1.create_window(200, 180, window=button1)

root.mainloop()