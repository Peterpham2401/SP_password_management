import sqlite3
import serect
from serect import decrypt, encrypt


# Suport Fuction

def get_AppName(app_name):
    try:
        connection = connectDB()
        cursor = connection.cursor()
        select_query = 'SELECT App_Name FROM account WHERE App_Name=?'
        cursor.execute(select_query, (app_name,))
        result = cursor.fetchall()
        list_app = list()
        for tmpapp in result:
            list_app.append(tmpapp[0])
        connection.commit()
        cursor.close()
        return list_app
    except(Exception, sqlite3.Error) as error:
        print(error)


def get_UserName(app_name):
    try:
        connection = connectDB()
        cursor = connection.cursor()
        select_query = 'SELECT UserName FROM account WHERE App_Name=?'
        cursor.execute(select_query, (app_name,))
        result = cursor.fetchall()
        list_user = list()
        for tmpapp in result:
            list_user.append(tmpapp[0])
        connection.commit()
        cursor.close()
        return list_user
    except(Exception, sqlite3.Error) as error:
        print(error)


def get_PassWordbyApp(app_name):
    try:
        connection = connectDB()
        cursor = connection.cursor()
        select_query = 'SELECT Password FROM account WHERE App_Name=?'
        cursor.execute(select_query, (app_name,))
        result = cursor.fetchall()
        list_password = list()
        for tmpapp in result:
            list_password.append(tmpapp[0])
        connection.commit()
        cursor.close()
        return list_password
    except(Exception, sqlite3.Error) as error:
        print(error)


def get_PassWordbyUser(username):
    try:
        connection = connectDB()
        cursor = connection.cursor()
        select_query = 'SELECT Password FROM account WHERE UserName=?'
        cursor.execute(select_query, (username,))
        result = cursor.fetchall()
        list_password = list()
        for tmpapp in result:
            list_password.append(tmpapp[0])
        connection.commit()
        cursor.close()
        return list_password
    except(Exception, sqlite3.Error) as error:
        print(error)


def checkExists(app_name):
    try:
        connection = connectDB()
        cursor = connection.cursor()
        select_query = 'SELECT App_Name FROM account'
        cursor.execute(select_query)
        result = cursor.fetchall()
        list_app = list()
        for tmpapp in result:
            list_app.append(tmpapp[0])
        for checkApp in list_app:
            if checkApp == app_name:
                return True
    except (Exception, sqlite3.Error) as error:
        print(error)
    finally:
        connection.commit()
        cursor.close()


def connectDB():
    try:
        connection = sqlite3.connect('PasswordManager.sqlite')
        return connection
    except(Exception, sqlite3.Error) as error:
        print(error)


# Main Function

def store_passwords(username, password, url, app_name):
    try:
        # app_name=app_name.trip()
        password = encrypt(password)
        connection = connectDB()
        cursor = connection.cursor()
        insert_query = "INSERT INTO account (UserName,Password,Url,App_Name) VALUES (?,?,?,?);"
        data = (username, password, url, app_name,)
        cursor.execute(insert_query, data)
        connection.commit()
        cursor.close()
        return True
    except (Exception, sqlite3.Error) as error:
        print(error)


def find_password(app_name):
    try:
        if checkExists(app_name) == True:
            result = get_AppName(app_name)
            if len(result) > 1:
                list_user = get_UserName(app_name)
                i = 0
                for username in list_user:
                    i += 1
                    print(i, '-', username)
                fi_user = int(input('Enter user you want to find:'))
                for tmpuser in list_user:
                    while True:
                        list_password = get_PassWordbyApp(app_name)
                        if fi_user <= len(list_password):
                            break
                        else:
                            print('There is no user name: %s' % fi_user)
                print('Password is:' + decrypt(list_password[fi_user - 1]))
            else:
                list_password = get_PassWordbyApp(app_name)
                print('Password is:' + decrypt(list_password[0]))
        else:
            print('There is no app name: %s' % app_name)
    except(Exception, sqlite3.Error) as error:
        print(error)


def delete_password(app_name):
    try:
        if checkExists(app_name) == True:
            connection = connectDB()
            cursor = connection.cursor()
            list_app = get_AppName(app_name)
            if len(list_app) > 1:
                list_user = get_UserName(app_name)
                i = 0
                for username in list_user:
                    i += 1
                    print(i, '-', username)
                del_user = int(input('Enter user you want to remove:'))    
                for tmpuser in list_user:
                    if del_user <= len(list_user):
                        select_query = 'DELETE FROM account WHERE UserName=?'
                        cursor.execute(select_query, (list_user[del_user - 1],))
                    else:
                        print('There is no user name: %s' % del_user)
            else:
                select_query = 'DELETE FROM account WHERE App_Name=?'
                cursor.execute(select_query, (app_name,))
            return True
        else:
            print('There is no app name:', app_name, '')
    except(Exception, sqlite3.Error) as error:
        print(error)
    

def All_App():
    try:
        connection = connectDB()
        cursor = connection.cursor()
        select_query = "SELECT App_Name, UserName FROM account ORDER BY App_Name ASC, UserName ASC;"
        cursor.execute(select_query)
        connection.commit()
        result = cursor.fetchall()
        if len(result) == 0:
            print('There is no App Stored in Database !!')
        i = 0
        for app in result:
            i += 1
            print(i, '-', app[0], '-', app[1])
    except(Exception, sqlite3.Error) as error:
        print(error)
