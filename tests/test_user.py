import unittest
from .app import db
from app.models import User

class Usertest(unittest.Testcase):
    '''
    Test to test the behaviour of the User class
    '''
    def setUp(self):
        '''
        Setup method to run before each test
        '''
        self.new_user=User(id=1,username='Lorna',email='kimanilorna@yahoo.com',password_hash='123',bio='I love programming',)

    def test_check_instance_variables(self):
        self.assertEquals(self.new_user.id,'1')
        self.assertEquals(self.new_user.username,'Lorna')
        self.assertEquals(self.new_user.password_hash,'123')
        self.assertEquals(self.new_user.email,"kimanilorna@yahoo.com")
        self.assertEquals(self.new_user.bio,'I love programming')

    def test_save_user(self):
        self.new_user.save_user()
        self.assertTrue(len(User.query.all())>0)

    def test_get_user(self):
        self.new_user.save_user()
        fetched_user = User.get_user(1)
        self.assertTrue(len(fetched_user) == 1)
