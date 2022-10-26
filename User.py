class User:
    def __init__(self, permissions, id, username, password, type):
        self.permissions = permissions
        self.id = id
        self.username = username
        self.password = password
        self.type = type
        self.access = False


    def login(self, username, password):
        if username == self.username and password == self.password:
            print(f'login for username{self.username} was successful')
            self.access = True
            return True
        else:
            return False


    def fillApplication(self, application):
        #call one of the application.fill functions here
        return