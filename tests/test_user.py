import unittest
from tests import BaseTestCase
from flask import json
import psycopg2



class AuthTest(BaseTestCase):

    def test_register_valid_details(self):
        """ Tests creating a new user with valid details """
        test_user = {
            'name': 'Rita',
            'username': 'Rhytah',
            'password': 'pass'
        }
        response = self.test_client.post('/api/v2/auth/register',data=json.dumps(test_user),
        content_type='application/json')
        self.assertEqual(response.status_code, 404)



    def test_register_with_blank_inputs(self):
        """ Tests creating a new user with blank """
        inv_char = {
            'name': '',
            'username': ' ',
            'password': ''
        }
        response = self.test_client.post('/api/v2/auth/register',
                                    data=json.dumps(inv_char),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_register_non_json_input(self):
        """ Tests register with non valid JSON input """
        response = self.test_client.post('/api/v2/auth/register',
                                    data='some non json data',
                                    content_type='application/json')
        self.assertEqual(response.status_code, 404)


    def test_login_valid_credentials(self):
        """ Tests login with valid credentials """
        user = {
            'username': 'Rhytah', 
            'password': 'pass'
        }
        response = self.test_client.post('/api/v2/auth/login',data=json.dumps(user),content_type='application/json')
        self.assertEqual(response.status_code, 200)
        # self.assertTrue(data['access_token'])

    # def test_login_invalid_characters(self):
    #     """ Test login with invalid characters """
    #     inv_char = {
    #         'username': '#$%',
    #         'password': '@#$%'
    #     }
    #     response = self.test_client.post('/api/v2/auth/login',
    #                                 data=json.dumps(inv_char),
    #                                 content_type='application/json')
    #     self.assertEqual(response.status_code, 406)

    def test_login_with_blank_inputs(self):
        """ Tests creating a new user with blank """
        inv_char = {

            'username': ' ',
            'password': ''
        }
        response = self.test_client.post('/api/v2/auth/login',
                                    data=json.dumps(inv_char),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)

    
    def test_login_invalid_password(self):
        """ Tests login with wrong password  """
        user = {
            'name': 'right user',
            'username': 'rightuser',
            'password': 'rightpassword'
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