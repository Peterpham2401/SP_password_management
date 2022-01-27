import database_manager
import os
from serect import vertify
from getpass import getpass


# SUPPORT FUNCTION
def login():
    input_pass = getpass(prompt='Enter 4 number pass to unlock:')
    if vertify(input_pass) == True:
        print('Unlock succesfull!!')
        clear()
        return True


def clear():
    enter = input('...Press Any Character to continue...')
    os.system('cls')


# MAIN FUNCTION 
def menu():
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


def create():
    app_name = (str(input('Enter app you want to save password:'))).strip()
    username = str(input('Enter User Name of %s app:' % app_name))
    password = str(input('Enter password of %s:' % app_name))
    url = str(input('Please coppy website url you want to save:'))
    if database_manager.store_passwords(username, password, url, app_name) == True:
        print('Create account %s succesfull !!' % username)
        clear()
    else:
        print('Create Falied!! Please check again')
        clear()


def find():
    find_name = str(input('Enter which app you want to find:'))
    database_manager.find_password(find_name)
    clear()


def printAllApp():
    database_manager.All_App()
    clear()


def delete():
    del_app = str(input('Enter App you want to remove: '))
    if database_manager.delete_password(del_app) == True:
        print('Delete succesfull !! ')
        clear()
    else:
        print('Delete Failed !! Please check again')
        clear()
