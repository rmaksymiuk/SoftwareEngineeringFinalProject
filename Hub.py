class Hub:
    def __init__(self):
        return

    def loginMenu(self, user):
        username = None
        password = None
        print(f'Please enter your username: {input(username)} ')
        print(f'Please enter your password: {input(password)}' )
        if user.login(username, password):
            self.mainMenu()
        else:
            print("Sorry, there seems to be a problem with you username or pasword")
            print("Please try again")

    def mainMenu(self):
        print('1. Create a form')
        print('2. Show current form')
        print('3. Show my profile')

