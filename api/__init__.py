from api.views import app
from api.models.api_models import Question,Answer,User

import unittest

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.test_client = app.test_client()

        self.request_data={
            "question_id":1,
            "subject": "problem",
            "asked_by":"Rhytah",
        }

        self.answer_data= {
            "answer_id":1,
            "question_id":1,
            "answered_by":"Namono",
            "description":"Solve a problem by finding it's root",
        }

        self.user_data={
            "user_id":1,
            "name":"Rita",
            "username":"Rhytah",
            "password":"pass"
            
        }

if __name__ == "__main__":
    unittest.main()



