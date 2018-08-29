from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Register(Resource):
    def post(self):
        return {'message': 'Register user'}

api.add_resource(Register, '/auth/signup')

class Login(Resource):
    def post(self):
        return {'messgae':'user login'}

api.add_resource(Login, '/auth/login')

class Allquestions(Resource):
    def get(self):
        return {'message':'Fetch all questions'}

    def post(self):
        return {'message': 'Add questions'}

api.add_resource(Allquestions, '/api/v2/questions')

class Specific_question(Resource):
    def get(self, question_id):
        return {'message':'fetch a specific question'}

    def delete(self,question_id):
        return {'message':'delete a question'}

api.add_resource(Specific_question, '/api/v2/questions/question_id')

class Answertoqtn(Resource):
    def post(self, question_id):
        return {'message':'post an answer to a question'}

api.add_resource(Answertoqtn, '/api/v2/questions/question_id/answers')


if __name__ == '__main__':
    app.run(debug=True)