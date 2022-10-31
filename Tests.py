import unittest
from User import User
from Database import Database

class Tests(unittest.TestCase):
    def testUser(self):
        user = User('Roman123', 'password')
        assert user.login('Roman123', 'password') is True
        assert user.login('ROman123', 'password') is False

    def testUserFromDatabase(self):
        database = Database()
        database = Database()
        database.loadDatabase()
        database.loadPermissions()

        assert len(database.fileList) == 4
        assert len(database.userList) == 4

    def testUserFromDatabase2(self):
        database = Database()
        database = Database()
        database.loadDatabase()
        database.loadPermissions()

        assert database.userList.get('Bob123') == '123qwe'
        assert database.userList.get('Tim1000') == '12345qwert'
        assert database.userList.get('John333') == '123456qwerty'
        assert database.userList.get('Grant111') == '1234qwer'

    def testUserFromDataBase3(self):
        database = Database()
        database = Database()
        database.loadDatabase()
        database.loadPermissions()

        assert len(database.permissions) == 4
        assert isinstance(database.permissions.get('Bob123')[1], list) == True

    # def testHub(self):
    #     return