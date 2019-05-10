class Users:
    userslist = []

    def __init__(self, login_username,login_password):

        self.login_username = login_username
        self.login_password = login_password

    def saveusers(self,username,password):
        Users.userslist.append(username)
        Users.userslist.append(password)
        print('user saved successfully')        