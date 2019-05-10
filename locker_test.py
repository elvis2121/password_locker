import unittest
from users import Users



class TestUsers(unittest.TestCase):

    def setUp(self):
        
        self.newuser = Users('mongoose2121','kenyan001')

    def test_init(self):

        self.assertEqual(self.newuser.login_username,'mongoose2121')
        self.assertEqual(self.newuser.login_password,'kenyan001')
    
    def test_saveuser(self):
        self.newuser.saveusers('','')
        self.assertEqual(len(Users.userslist),+2)    

       


if __name__ == '__main__':
    unittest.main()