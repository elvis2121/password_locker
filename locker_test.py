import unittest
from users import Users
from credentials import Credentials



class TestLocker(unittest.TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        
        self.newuser = Users('mongoose2121','kenyan001')
        self.newcredentials = Credentials('twitter','marto','martin123')

    def test_createuser(self):
        '''
        Method to check whether user has been created successfully.
        '''

        self.assertEqual(self.newuser.login_username,'mongoose2121')
        self.assertEqual(self.newuser.login_password,'kenyan001')
    
    def test_saveuser(self):
        '''
        method to test whether user has been saved in the list
        '''
        self.newuser.saveusers('','')
        self.assertEqual(len(Users.userslist),+2)    

    def test_deleteuser(self):
        '''
        Method to test whether user can be deleted
        '''
        self.newuser.saveusers('kevo','kevo123')
        self.newuser.deleteuser('kevo','kevo123')
        self.assertEqual(len(Users.userslist),0)


    def test_createcredentials(self):
        '''
        Method to check whether credentials have been created successfully.
        '''
        self.assertEqual(self.newcredentials.app_name,'twitter')
        self.assertEqual(self.newcredentials.app_username,'marto')
        self.assertEqual(self.newcredentials.app_password,'martin123')  

    def test_savecredentials(self):
        '''
        Method to check whether credentilas have been saved successfully.
        '''
        self.newcredentials.savecredentials('facebook','elvo','elvo123')
        self.assertEqual(len(Credentials.credentials_list),+3) 

    def test_deletecredentials(self):
        '''
        Method to check whether credentials have been deleted successfully.
        '''
        self.newcredentials.savecredentials('tinder','johny','johny123')
        self.newcredentials.deletecredentials('tinder','johny','johny123') 
        self.assertEqual(len(Credentials.credentials_list),0)   


if __name__ == '__main__':
    unittest.main()