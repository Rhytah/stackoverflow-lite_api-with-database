from flask import Flask,request,jsonify,make_response
#from flask_restful import Resource, Api
from .models.api_models import User
from api.models.database import DbManager


app = Flask(__name__)
#api = Api(app)
dbmanager=DbManager()

# class Register(Resource):def post(self):
@app.route('/api/v2/auth/signup', methods =['POST'])
def user_signup():
    
        user_data = request.get_json()
        name = user_data['name']
        username = user_data['username']
        password = user_data['password']

        if not user_data:
            return jsonify({'status':'Fail',
                  'message':'All fields are required'})

        if not name or name == "  ":
            return jsonify({"message": 'Invalid, Please enter a correct name'})

        if not username or username == "  ":
            return jsonify({"message": 'Invalid, Please enter a valid username'}) 

        if not password or password == "  ":
            return jsonify({"message": 'Invalid, Please enter a correct password'})

        if dbmanager.get_by_argument(name,username,password):
            return jsonify({'message':'User already exists'})
        dbmanager.register_user(name,username,password)
        return jsonify({'message':'user added successfully'}),201

@app.route('/api/v2/auth/login', methods =['POST'])
def login_user():
    user_data=request.get_json()
    name=data['name']
    username=data['username']
    password=data['password']
    dbmanager_query=dbmanager.get_by_argument('users','username',username)
    user=User(dbmanager_query[0], dbmanager_query[1], dbmanager_query[2], dbmanager_query[3])


    
# api.add_resource(Register, '/api/v2/auth/signup')

# class Login(Resource):
#     def post(self):
#         return {'messgae':'user login'}

# api.add_resource(Login, '/auth/login')

# class Allquestions(Resource):
#     def get(self):
#         request_data=request.get_json()

#         return {'message':'Fetch all questions'}

#     def post(self):
#         return {'message': 'Add questions'}

# api.add_resource(Allquestions, '/api/v2/questions')

# class Specific_question(Resource):
#     def get(self, question_id):
#         return {'message':'fetch a specific question'}

#     def delete(self,question_id):
#         return {'message':'delete a question'}

# api.add_resource(Specific_question, '/api/v2/questions/question_id')

# class Answertoqtn(Resource):
#     def post(self, question_id):
#         return {'message':'post an answer to a question'}

# api.add_resource(Answertoqtn, '/api/v2/questions/question_id/answers')


if __name__ == '__main__':
    app.run(debug=True)
    # db=DbManager()
    # db.create_tables()
    
