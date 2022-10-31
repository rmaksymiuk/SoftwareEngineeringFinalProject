import tkinter as tk
from tkinter import ttk
from Home import HomePage


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


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
        currentUser = User(username, password)
        # heading
        heading = ttk.Label(self, text='Member Login', style='Heading.TLabel')
        heading.grid(column=0, row=0, columnspan=2, pady=5, sticky=tk.N)

        # username
        username_label = ttk.Label(self, text="Username:")
        username_label.grid(column=0, row=1, sticky=tk.W, **paddings)
        username_entry = ttk.Entry(self, textvariable=username, **entry_font)
        username_entry.grid(column=1, row=1, sticky=tk.E, **paddings)
        # password
        password_label = ttk.Label(self, text="Password:")
        password_label.grid(column=0, row=2, sticky=tk.W, **paddings)
        password_entry = ttk.Entry(
            self, textvariable=password, show="*", **entry_font)
        password_entry.grid(column=1, row=2, sticky=tk.E, **paddings)

        # login button
        login_button = ttk.Button(self, text="Login", command= lambda:loginCheck(currentUser))
        login_button.grid(column=1, row=3, sticky=tk.E, **paddings)

        # configure style
        self.style = ttk.Style(self)
        self.style.configure('TLabel', font=('Helvetica', 11))
        self.style.configure('TButton', font=('Helvetica', 11))
        # heading style
        self.style.configure('Heading.TLabel', font=('Helvetica', 12))

        def loginCheck(User):
            print("1111111")
            User.username = username_entry.get()
            User.password = password_entry.get()
            if User.username == User.password:  #Please add your checking on username and password code here!
                # if user.login(username, password):
                print("Log in successfully!")
                # Redirecting to main menu
                Main = Hub().mainMenu()
            else:
                print(currentUser.username)
                print("Sorry, there seems to be a problem with you username or password")
                print("Please try again")


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


