import menu

if menu.login() == True:
    while True:
        choice = menu.menu()
        if (choice == 1):
            menu.create()
        if (choice == 2):
            menu.find()
        if (choice == 3):
            menu.printAllApp()
        if (choice == 4):
            menu.delete()
        if (choice == 5):
            break
else:
    print('Wrong password!!!')
    exit()
