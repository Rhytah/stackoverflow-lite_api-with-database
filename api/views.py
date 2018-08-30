from flask import Flask,request,jsonify,make_response
from .models.api_models import User, Question
from api.models.database import DbManager
from datetime import datetime,timedelta
from flask_jwt_extended import(JWTManager,jwt_required,create_access_token,get_jwt_identity)



app = Flask(__name__)
 #setup flask-jwt-extened entension
app.config['JWT_SECRET_KEY'] = 'rhytahz'
jwt = JWTManager(app)
dbmanager=DbManager()


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

    
    dbmanager.register_user(name,username,password)
    return jsonify({'message':'user added successfully'}),201

@app.route('/api/v2/auth/login', methods =['POST'])
def login_user():
    user_data=request.get_json()
    #name=user_data['name']
    username=user_data['username']
    password=user_data['password']
    dbmanager_query=dbmanager.get_by_argument('users','username',username)
    # user=User(dbmanager_query[0], dbmanager_query[1], dbmanager_query[2], dbmanager_query[3])
    
    # print (user)
    if not username:
        return jsonify({"msg" : "Provide Valid Username"}),400

    if not password:
        return jsonify({"msg" : "Incorrect password"}),400

    # if username !='test' or password !='test':
    #     return jsonify({"msg": "Invalid username or password"})

    access_token= create_access_token(identity=username)
    return jsonify(access_token=access_token),200

@app.route('/api/v2/protected', methods =['GET'])
@jwt_required
def protected():
    #access the identity of current user
    current_user=get_jwt_identity()
    return jsonify(loggesd_in_as=current_user),200
    
    # if user.username ==user_data['username']:
    #     token = jwt.encode(
    #                     {'username': user.username,
    #                      'exp': datetime.utcnow() +
    #                      timedelta(days=10, minutes=60)
    #                      }, 'mysecret')
    #     if token:
    #         response = {
    #             'message': 'You logged in successfully.',
    #             'token': token.decode('UTF-8'),
    #             'name': user.name,
    #             'username': user.username,
    #             'user_id': user.user_id
    #         }
    #     return make_response(jsonify(response)), 200
        
    # return jsonify({'message':'Invalid username or password, try again or create an account'}), 401

@app.route('/api/v2/questions', methods =['GET'])
@jwt_required
def fetch_questions():
    questions= dbmanager.get_questions()   
    if len(questions)<1:
        return jsonify({
            "status":'Fail',
            "message":'There are no questions'
        }),404

    if len(questions)>=1:
        return jsonify({
            "message":'Here are the questions',
            "questions":questions
        }),200
 
    return jsonify({'questions':questions})
@app.route('/api/v2/questions', methods=['POST'])
@jwt_required
def add_question():
    #questions=dbmanager.get_questions()
    request_data=request.get_json()
    #question_id=len(questions)+1
    subject=request_data['subject']
    asked_by=request_data['asked_by']
    
    question= dbmanager.addon_question(subject,asked_by)
    return jsonify({'message':'Your question has been posted'})


@app.route('/api/v2/question/<int:question_id>', methods=['GET'])
@jwt_required
def fetch_a_question(question_id):
    
    question=dbmanager.get_a_question()
    for Specific_question in questions:
        if Specific_question.get(id)==question_id:
            return jsonify({'message': Specific_question})

    return jsonify({
        'status':'Fail',
        'message':'Question doesnot exist'
    })
    




    
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
    
