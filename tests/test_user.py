import unittest
from tests import BaseTestCase
from flask import json
import psycopg2



class AuthTestcase(BaseTestCase):

    def test_register_valid_details(self):
        
        test_user = {
            'name': 'Rita',
            'username': 'Rhytah',
            'password': 'pass'
        }
        response = self.test_client.post('/api/v2/auth/register',data=json.dumps(test_user),
        content_type='application/json')
        self.assertEqual(response.status_code, 404)


    def test_register_non_json_input(self):

        response = self.test_client.post('/api/v2/auth/register',
                                    data='some non json data',
                                    content_type='application/json')
        self.assertEqual(response.status_code, 404)


    def test_login_valid_credentials(self):
        
        user = {
            'username': 'Rhytah', 
            'password': 'pass'
        }
        response = self.test_client.post('/api/v2/auth/login',data=json.dumps(user),content_type='application/json')
        self.assertEqual(response.status_code, 200)

    
    def test_login_invalid_password(self):
        
        user = {
            'name': 'something',
            'username': 'anything',
            'password': 'anypassword'
        }
        self.test_client.post('/api/v2/auth/register',
                         data=json.dumps(user),
                         content_type='application/json')
        user_login = {
            'username': 'Rhytah',
            'password': 'wrongpassword'
        }
        response = self.test_client.post('/api/v2/auth/login',
                                    data=json.dumps(user_login),
                                    content_type='application/json')

        self.assertIn(
            'Invalid username or password',
            str(response.data))
        self.assertEqual(response.status_code, 200)