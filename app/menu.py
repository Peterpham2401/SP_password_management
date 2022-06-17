from Database_Manager import Database
import os
from serect import vertify
from getpass import getpass


# SUPPORT FUNCTION
class menu():
    def clear(self):
        enter = input('...Press Any Character to continue...')
        os.system('clear')

    def login(self):
        input_pass = getpass(prompt='Enter 4 number pass to unlock:')
        if vertify(input_pass) == True:
            self.database_manager = Database()
            print('Unlock succesfull!!')
            self.clear()
            return True

    # MAIN FUNCTION
    def menu(self):
        print('-' * 33)
        print('-' * 13, 'MENU', '-' * 14)
        print('| 1-Create new password         |')
        print('| 2-Find a password by app name |')
        print('| 3-List all app name           |')
        print('| 4-Delet a app                 |')
        print('| 5-Quit                        |')
        print('-' * 33)
        choice = int(input('Enter your choice:'))
        return choice


    def create(self):
        app_name = (str(input('Enter app you want to save password:'))).strip()
        username = str(input('Enter User Name of %s app:' % app_name))
        password = str(input('Enter password of %s:' % app_name))
        url = str(input('Please coppy website url you want to save:'))
        if self.database_manager.store_passwords(username, password, url, app_name) == True:
            print('Create account %s succesfull !!' % username)
            self.clear()
        else:
            print('Create Falied!! Please check again')
            self.clear()


    def find(self):
        find_name = str(input('Enter which app you want to find:'))
        self.database_manager.find_password(find_name)
        self.clear()


    def printAllApp(self):
        self.database_manager.All_App()
        self.clear()


    def delete(self):
        del_app = str(input('Enter App you want to remove: '))
        if self.database_manager.delete_password(del_app) == True:
            print('Delete succesfull !! ')
            self.clear()
        else:
            print('Delete Failed !! Please check again')
            self.clear()
