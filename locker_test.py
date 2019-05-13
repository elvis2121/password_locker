import unittest
from users import Users
from credentials import Credentials



class TestLocker(unittest.TestCase):

    def setUp(self):
        
        self.newuser = Users('mongoose2121','kenyan001')
        self.newcredentials = Credentials('twitter','marto','martin123')

    def test_createuser(self):

        self.assertEqual(self.newuser.login_username,'mongoose2121')
        self.assertEqual(self.newuser.login_password,'kenyan001')
    
    def test_saveuser(self):
        self.newuser.saveusers('','')
        self.assertEqual(len(Users.userslist),+2)    

    def test_deleteuser(self):
        self.newuser.saveusers('kevo','kevo123')
        self.newuser.deleteuser('kevo','kevo123')
        self.assertEqual(len(Users.userslist),0)

    def test_createcredentials(self):
        self.assertEqual(self.newcredentials.app_name,'twitter')
        self.assertEqual(self.newcredentials.app_username,'marto')
        self.assertEqual(self.newcredentials.app_password,'martin123')  

    def test_savecredentials(self):
        self.newcredentials.savecredentials('facebook','elvo','elvo123')
        self.assertEqual(len(Credentials.credentials_list),+3)   


if __name__ == '__main__':
    unittest.main()