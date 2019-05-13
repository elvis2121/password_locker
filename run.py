from users import Users
from credentials import Credentials
import random


print('WELCOME TO PASSWORD LOCKER')
print('-' *30)

credentials1 = Credentials('','','')
user1 = Users('','')

random1 = random

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

                dashboard3()

                

        def createcredentials(appname,appusername,apppassword):
                
                credentials1 = Credentials(appname,appusername,apppassword)

        def dashboard3():
                credentials1.app_name = input('enter app name: ')
                credentials1.app_username = input('enter app username: ')

                print('select a choice:\n ag - autogenerate password, sp - setpassword ')
                choice3 =input()

                if choice3 == 'ag':
                        credentials1.app_password = random1.randint(0,100000)
                        print('auto generated password is: {} '.format(credentials1.app_password))
                                 
                        createcredentials(credentials1.app_name,credentials1.app_username,credentials1.app_password)
                        credentials1.savecredentials(credentials1.app_name,credentials1.app_username,credentials1.app_password)

                if choice3 == 'sp':
                        credentials1.app_password = input('enter your password: ')
                        print('your password is: {} '.format(credentials1.app_password))

                        createcredentials(credentials1.app_name,credentials1.app_username,credentials1.app_password)
                        credentials1.savecredentials(credentials1.app_name,credentials1.app_username,credentials1.app_password)


        def dashboard2():

                print('select a choice:\n ac - add credentials, dc - display credentials, dl - delete credentials')
                choice2=input()

                if choice2 == 'ac':
                        dashboard3()
                        dashboard2()

                if choice2 == 'dc':
                        Credentials.displaycredentials()
                        dashboard2()

                if choice2 == 'dl':
                        credentials1.app_name = input('enter appname of account to be deleted: ')
                        credentials1.app_username = input('enter username of account to be deleted: ')
                        credentials1.app_password = input('enter password of account to be deleted: ')
                        credentials1.deletecredentials(credentials1.app_name,credentials1.app_username,credentials1.app_password)        

                if (choice2 != 'ac' and choice2 != 'dc' and choice2 !='dl'):
                        print('invalid choice!!!!')
                        dashboard2()          

        def dashboard():
                print('What would you like to do? \n rg - register account, lg - login, dl- delete account')
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
                
                if choice1 == 'dl':
                        user1.login_username = input('enter username of account to be deleted: ')
                        user1.login_password = input('enter password of account to be deleted: ')
                        user1.deleteuser(user1.login_username,user1.login_password)

                if (choice1 != 'rg' and choice1 != 'lg' and choice1 != 'dl'):
                        print('invalid choice!!!!')
                        dashboard()    



        dashboard()
             
if __name__ == '__main__':

    main()


