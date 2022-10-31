import tkinter as tk
from tkinter import ttk
from Home import HomePage

UsernameInput = None
PasswordInput = None

def loginCheck():
    print("1111111")
    if UsernameInput == 1:
        # if user.login(username, password):
        print("Log in successfully!")
        Main = Hub().mainMenu()
    else:
        print(UsernameInput)
        print("Sorry, there seems to be a problem with you username or password")
        print("Please try again")


class Login(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('300x150')
        self.resizable(0, 0)
        self.title('SEP Login')

        # UI options
        paddings = {'padx': 5, 'pady': 5}
        entry_font = {'font': ('Helvetica', 11)}

        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        username = tk.StringVar()
        password = tk.StringVar()

        # heading
        heading = ttk.Label(self, text='Member Login', style='Heading.TLabel')
        heading.grid(column=0, row=0, columnspan=2, pady=5, sticky=tk.N)

        # username
        username_label = ttk.Label(self, text="Username:")
        username_label.grid(column=0, row=1, sticky=tk.W, **paddings)
        username_entry = ttk.Entry(self, textvariable=username, **entry_font)
        username_entry.grid(column=1, row=1, sticky=tk.E, **paddings)
        UsernameInput = username_entry.get()

        # password
        password_label = ttk.Label(self, text="Password:")
        password_label.grid(column=0, row=2, sticky=tk.W, **paddings)
        password_entry = ttk.Entry(
            self, textvariable=password, show="*", **entry_font)
        password_entry.grid(column=1, row=2, sticky=tk.E, **paddings)
        PasswordInput = password_entry.get()

        # login button
        login_button = ttk.Button(self, text="Login", command=loginCheck)
        login_button.grid(column=1, row=3, sticky=tk.E, **paddings)

        # configure style
        self.style = ttk.Style(self)
        self.style.configure('TLabel', font=('Helvetica', 11))
        self.style.configure('TButton', font=('Helvetica', 11))

        # heading style
        self.style.configure('Heading.TLabel', font=('Helvetica', 12))


class Hub:
    def __init__(self):
        return

    def loginMenu(self):
        app = Login()
        app.mainloop()

    def mainMenu(self):
        root = HomePage()
        root.mainloop()


if __name__ == "__main__":
    login = Hub().loginMenu()
