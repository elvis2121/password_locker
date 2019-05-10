from users import Users


print('WELCOME TO PASSWORD LOCKER')
print('-' *10)
print('What would you like to do? \n rg - register account, lg - login,')

user1 = Users('','')
choice1 = input()


if choice1 == 'rg':
    username = input("enter your username: ")
    password = input("enter your password: ")
    print("your username is {} and password is {}".format(username,password))

    user1.saveusers(username,password)




    








