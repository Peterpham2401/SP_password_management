import sqlite3
import serect
from serect import decrypt, encrypt


class Database():
    def __init__(self):
        try:
            self.connection = sqlite3.connect('PasswordManager.sqlite')
            self.cursor = self.connection.cursor()
            create_query = """CREATE TABLE IF NOT EXISTS account(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                UserName TEXT NOT NULL,
                Password TEXT NOT NULL,
                Url TEXT NOT NULL,
                App_Name TEXT NOT NULL
            );"""
            self.cursor.execute(create_query)
            self.connection.commit()
        except(Exception, sqlite3.Error) as error:
            print(error)

    #Support Function
    def get_AppName(self,app_name):
        try:
            select_query = "SELECT App_Name FROM account WHERE App_Name=?"
            self.cursor.execute(select_query,(app_name,))
            result = self.cursor.fetchall()
            list_app = list()
            for tmpapp in result:
                list_app.append(tmpapp[0])
            self.connection.commit()
            return list_app
        except(Exception, sqlite3.Error) as error:
            print(error)


    def get_UserName(self,app_name):
        try:
            select_query = "SELECT UserName FROM account WHERE App_Name=?"
            self.cursor.execute(select_query,(app_name,))
            result = result = self.cursor.fetchall()
            list_user = list()
            for tmpapp in result:
                list_user.append(tmpapp[0])
            self.connection.commit()
            return  list_user
        except(Error, sqlite3.Error) as error:
            print(error)

    def get_PassWordbyApp(self,app_name):
        try:
            select_query = 'SELECT Password FROM account WHERE App_Name=?'
            self.cursor.execute(select_query, (app_name,))
            result = self.cursor.fetchall()
            list_password = list()
            for tmpapp in result:
                list_password.append(tmpapp[0])
            self.connection.commit()
            return list_password
        except(Exception, sqlite3.Error) as error:
            print(error)

    def get_PassWordbyUser(self,username):
        try:
            select_query = 'SELECT Password FROM account WHERE UserName=?'
            self.cursor.execute(select_query, (username,))
            result = self.cursor.fetchall()
            list_password = list()
            for tmpapp in result:
                list_password.append(tmpapp[0])
            self.connection.commit()
            self.cursor.close()
            return list_password
        except(Exception, sqlite3.Error) as error:
            print(error)

    def checkExists(self,app_name):
        try:
            select_query = 'SELECT App_Name FROM account'
            self.cursor.execute(select_query)
            result = self.cursor.fetchall()
            list_app = list(tmpapp[0] for tmpapp in result)
            for checkApp in list_app:
                if checkApp == app_name:
                    return True
        except (Exception, sqlite3.Error) as error:
            print(error)

    #Main Function
    def store_passwords(self,username, password, url, app_name):
        try:
            app_name=str(app_name).strip()
            password = encrypt(str(password).strip())
            insert_query = "INSERT INTO account (UserName,Password,Url,App_Name) VALUES (?,?,?,?);"
            data = (username, password, url, app_name,)
            self.cursor.execute(insert_query, data)
            self.connection.commit()
            return True
        except (Exception, sqlite3.Error) as error:
            print(error)

    def find_password(self,app_name):
        try:
            if self.checkExists(app_name) == True:
                result = self.get_AppName(app_name)
                if len(result) > 1:
                    list_user = self.get_UserName(app_name)
                    index_user= 0
                    for username in list_user:
                        index_user+= 1
                        print(index_user, '-', username)
                    fi_user = int(input('Enter user you want to find:'))
                    for tmpuser in list_user:
                        while True:
                            list_password = self.get_PassWordbyApp(app_name)
                            if fi_user <= len(list_password):
                                break
                            else:
                                print('There is no user name: %s' % fi_user)
                    print('Password is:' + decrypt(list_password[fi_user - 1]))
                else:
                    list_password = self.get_PassWordbyApp(app_name)
                    print('Password is:' + decrypt(list_password[0]))
            else:
                print('There is no app name: %s' % app_name)
        except(Exception, sqlite3.Error) as error:
            print(error)

    def delete_password(self,app_name):
        try:
            if self.checkExists(app_name) == True:
                list_app = self.get_AppName(app_name)
                if len(list_app) > 1:
                    list_user = self.get_UserName(app_name)
                    index_user = 0
                    for username in list_user:
                        index_user+= 1
                        print(index_user, '-', username)
                    del_user = int(input('Enter user you want to remove:'))
                    for tmpuser in list_user:
                        if del_user <= len(list_user):
                            select_query = 'DELETE FROM account WHERE UserName=?'
                            self.cursor.execute(select_query, (list_user[del_user - 1],))
                            self.connection.commit()
                        else:
                            print('There is no user name: %s' % del_user)
                else:
                    select_query = 'DELETE FROM account WHERE App_Name=?'
                    self.cursor.execute(select_query, (app_name,))
                    self.connection.commit()
                return True
            else:
                print('There is no app name:', app_name, '')
        except(Exception, sqlite3.Error) as error:
            print(error)

    def All_App(self):
        try:
            select_query = "SELECT App_Name, UserName FROM account ORDER BY App_Name ASC, UserName ASC;"
            self.cursor.execute(select_query)
            self.connection.commit()
            result = self.cursor.fetchall()
            if len(result) == 0:
                print('There is no App Stored in Database !!')
            index_app= 0
            for app in result:
                index_app+= 1
                print(index_app, '-', app[0], '-', app[1])
        except(Exception, sqlite3.Error) as error:
            print(error)

