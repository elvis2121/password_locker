from users import Users


print('WELCOME TO PASSWORD LOCKER')

username = input("enter your username: ")
password = input("enter your password: ")
print("your username is {} and password is {}".format(username,password))

user1 = Users(username,password)
