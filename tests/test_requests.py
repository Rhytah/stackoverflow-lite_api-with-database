from tests import BaseTestCase

import json

from flask import jsonify

class RequestTestmodels(BaseTestCase):
    
    def test_get_all_questions(self):
        
        response=self.test_client.get(
            '/api/v2/questions', data=json.dumps(self.request_data),content_type='application/json'
        )
        self.assertEqual(response.status_code,401)
        
    def test_get_a_question(self):
        response=self.test_client.get(
            '/api/v2/questions/1', content_type='application/json'
        )
        self.assertEqual(response.status_code,401)
        

#without authorization
    def test_add_a_question(self):
        response=self.test_client.post(
            '/api/v2/questions', data = json.dumps(self.request_data),content_type='application/json')
        self.assertEqual(response.status_code,401)
        self.assertIn(
            "Missing Authorization Header", str(response.data)
        )
        
    def test_add_a_question_without_subject(self):
    
        response = self.test_client.post('/api/v2/questions',
        data=json.dumps({"question_id": 2 , "subject": " ","asked_by": "Tom", "question_date": "Yesterday"}),
        content_type='application/json')
        self.assertEqual(response.status_code,401)
        self.assertTrue('Please Indicate what you are asking about',str(response.data))

  
    def test_add_an_answer(self):
        response=self.test_client.post(
            '/api/v2/questions/1/answers', data = json.dumps(self.answer_data),content_type='application/json')
        self.assertEqual(response.status_code,404)

    def test_question_get(self):
            response = self.test_client.get( '/api/v1/questions/2', content_type='application/json' )
            # responseJson = json.loads( response.data.decode() )
            # self.assertEqual( "problem", responseJson[0]["Question"] )
            self.assertEqual( response.status_code, 404 )


    def test_add_an_answer_without_question_id(self):
        response = self.test_client.post('/api/v2/answers',
        data=json.dumps({"answer_id":2, "question_id": " " , "answered_by": "Gloria ","description": "Strive for excellence"}),
        content_type='application/json')
        self.assertEqual(response.status_code,404)      
        
    def test_modify_answer(self):
        response=self.test_client.put('/api/v2/questions/1/answers',data=json.dumps(self.answer_data), content_type='application/json')
        self.assertEqual(response.status_code,404)

    
    def test_get_answers(self):
            response=self.test_client.post(
                '/api/v2/answers', data= json.dumps(self.answer_data),content_type='application/json')
            response=self.test_client.get(
                '/api/v2/answers', data=json.dumps(self.answer_data),content_type='application/json')
            self.assertEqual(response.status_code,404)

