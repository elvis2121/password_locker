class Users:
    userslist = []

    def __init__(self, login_username,login_password):

        self.login_username = login_username
        self.login_password = login_password


    @classmethod
    def saveusers(cls,username, password):
        cls.userslist.append(username)
        cls.userslist.append(password)
        
        print('user saved successfully')
        print(Users.userslist)

    

          
    