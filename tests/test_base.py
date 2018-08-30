import unittest
import psycopg2
from flask import json
from api.models.database import DbManager
from api import app
app=flask(__name__)

class TestBase(unittest,TestCase):
        
        #create and add test user
        # self.user_test={'user_id':'','name': "Rita", 'username':'rita','password':password}
        # password_hash = generate_password_hash(password, method='sha256')
        # test_user = User(user_id='', name='Rita', username='rita', email='ritanamono@gmail.com',password=password_hash)


        ###############

    user = {
        'username': 'username',
        'email': 'email',
        'password': 'password'
    }

    valid_user = {
        'username': 'TestUser',
        'email': 'validemail',
        'password': 'password'
    }

    valid_question = {
        'title': 'math',
        'description': "why math",
        "date": "2018-11-12 12:49:00"
    }
    post_question = {
        'title': 'math',
        'description': "why math",
        "date": "2019-11-12 12:49:00"
    }
    def create_app(self):
        """
        Create an instance of the app with the testing configuration
        """
        app.config.from_object(app_config["testing"])
        return app

    def setUp(self):
        self.client = app.test_client(self)
        dbmanager = Database(
            'postgresql://postgres:0000@localhost:5432/stacko_testdb')
        dbmanager.create_tables()
        self.create_valid_user()

    def create_valid_user(self):
        """ Registers a user to be used for tests"""
        response = self.client.post('/api/v2/auth/register',
                                    data=json.dumps(self.valid_user),
                                    content_type='application/json')
        return response

    def get_token(self):
        ''' Generates a toke to be used for tests'''
        response = self.client.post('/api/v2/auth/login',
                                    data=json.dumps(self.valid_user),
                                    content_type='application/json')
        data = json.loads(response.data.decode())
        return data['token']

    def create_valid_question(self):
        """ Creates a valid question to be used for tests """
        response = self.client.post('api/v2/users/questions/',
                                    data=json.dumps(self.valid_question),
                                    content_type='application/json',
                                    headers={'Authorization':
                                             self.get_token()})
        return response

    def create_post_question(self):
        """ Creates a valid question to be used for tests """
        response = self.client.post('api/v2/users/questions/',
                                    data=json.dumps(self.post_question),
                                    content_type='application/json',
                                    headers={'Authorization':
                                             self.get_token()})
        return response

    def create_user(self):
        """ Registers a user to be used for tests"""
        response = self.client.post('/api/v2/auth/register',
                                    data=json.dumps(self.user),
                                    content_type='application/json')
        return response

    def user_token(self):
        ''' Generates a toke to be used for tests'''
        response = self.client.post('/api/v2/auth/login',
                                    data=json.dumps({
                                        'username': 'user',
                                        'password': 'password'}),
                                    content_type='application/json')
        data = json.loads(response.data.decode())
        return data['token']

    def tearDown(self):
        db = Database(
            'postgresql://postgres:0000@localhost/stacko_testdb')
        db.trancate_table("users")
        db.trancate_table("questions")
        db.trancate_table("answers")

    def tearDown(self):
        db.drop_all()

