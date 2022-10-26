from openpyxl import Workbook
import os, sys, subprocess
import pandas as pd
class Database:
    def __init__(self):
        self.fileList = []
        self.userList = {}
        self.path = 'Database/database.xlsx'

    def showDatabase(self):
        print(f'current applications: {self.fileList}')
        print(f'current users: {self.userList}')

    def addFile(self, file):
        self.fileList.append(file)

    def addUser(self, user):
        self.userList.update({user.username: user.password})

    def loadDatabase(self):
        sheet = "Sheet1"
        df = pd.read_excel(self.path, sheet_name=sheet)#usecols=['UsernameList', 'PasswordList', 'FileList']
        self.fileList = df['FileList'].tolist()
        self.userList = dict(zip(df.UsernameList, df.PasswordList))


