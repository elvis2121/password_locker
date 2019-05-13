class Credentials:
    credentials_list =[]

    def __init__(self,app_name,app_username,app_password):
        self.app_name = app_name
        self.app_username = app_username
        self.app_password = app_password

    
    def savecredentials(self,appname,username, password):
        self.credentials_list.append(appname)
        self.credentials_list.append(username)
        self.credentials_list.append(password)
        
        print('Credentials saved successfully!!!!!!!!!!!!!!!!')
        

    @classmethod
    def displaycredentials(cls):
        print(cls.credentials_list) 

    def deletecredentials(self,appname,username, password):
        for x in Credentials.credentials_list:
            if appname and username and password == x:
                Credentials.credentials_list.remove(appname)
                Credentials.credentials_list.remove(username)
                Credentials.credentials_list.remove(password)
                print('credentials deleted')
                print(Credentials.credentials_list)
        