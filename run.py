from users import Users
from credentials import Credentials


print('WELCOME TO PASSWORD LOCKER')
print('-' *30)

credentials1 = Credentials('','','')
user1 = Users('user1','user2')

def main():
                        
        def index():
                i = 0
                if i % 2 == 0:
                        return i

        def index2():
                m = 1
                if m % 2 == 1:
                        return round(m)


        def getuserinput(username,password):
                
                user1.login_username = input("enter your username: ")
                user1.login_password = input("enter your password: ")
                print("your username is {} and password is {}\n".format(user1.login_username,user1.login_password))
        

        def createuser(username,password):
                user1=Users(username,password) 

        def checkuser():
                
                if user1.login_username == Users.userslist[index()] and user1.login_password == Users.userslist[index2()]:
                        print('username and password passed')
                        dashboard2()
                else:
                        print('username and password donot match')
                        dashboard()

        def getcredentialsinput(appname,appusername,apppassword):

                credentials1.app_name = input('enter app name: ')
                credentials1.app_username = input('enter app username: ')
                credentials1.app_password =input('enter app password: ') 

        def createcredentials(appname,appusername,apppassword):
                credentials1 = Credentials(appname,appusername,apppassword)

        def displaycredentials():
                print(credentials1.savecredentials(credentials1.app_name,credentials1.app_username,credentials1.app_password))                       
        
       


        def dashboard2():

                print('select a choice:\n ac - add credentials, dc - display credentials')
                choice2=input()

                if choice2 == 'ac':
                        getcredentialsinput(credentials1.app_name,credentials1.app_username,credentials1.app_password)
                        createcredentials(credentials1.app_name,credentials1.app_username,credentials1.app_password)
                        credentials1.savecredentials(credentials1.app_name,credentials1.app_username,credentials1.app_password)
                        dashboard2()

                if choice2 == 'dc':
                        credentials1.displaycredentials()
                        dashboard2()
        

        def dashboard():
                print('What would you like to do? \n rg - register account, lg - login,')
                choice1 = input()


                if choice1 == 'rg':
                        getuserinput(user1.login_username,user1.login_password)
                        
                
                        createuser(user1.login_username,user1.login_password)
                        user1.saveusers(user1.login_username,user1.login_password)
                        print('*********USER SAVED**********\n')
                        print('*********proceed to login**********\n')
                        dashboard()

                if choice1 == 'lg':

                        getuserinput(user1.login_username,user1.login_password)        
                        checkuser()
                

                if (choice1 != 'rg' and choice1 != 'lg'):
                        print('invalid choice!!!!')
                        dashboard()    



        dashboard()
             
if __name__ == '__main__':

    main()


