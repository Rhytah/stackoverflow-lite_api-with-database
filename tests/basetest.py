import unittest
from app import create_app, db

class BaseTestCase(unittest,TestCase):
    def setup(self):
        self.app = create_app("testing")
        self.test_client = self.app.test_client()
        
        db.create_all()
        
        #test login
        self.user = {'username':'rita','password':'something'}
        
        #create and add test user
        password= 'something'
        self.user_test={'user_id':'','name': "Rita", 'username':'rita','email':'ritanamono@gmail.com','password':password}
        password_hash = generate_password_hash(password, method='sha256')
        test_user = User(user_id='', name='Rita', username='rita', email='ritanamono@gmail.com',password=password_hash)
        save(test_user) 

    def tearDown(self):
        db.drop_all()

