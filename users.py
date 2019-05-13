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

    def deleteuser(self,username, password):
        for x in Users.userslist:
            if username and password == x:
                Users.userslist.remove(username)
                Users.userslist.remove(password)
                print('account deleted')
                print(Users.userslist)


    

          
    