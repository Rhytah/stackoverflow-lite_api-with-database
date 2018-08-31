from flask import Flask,request,jsonify,make_response
from .models.api_models import User, Question
from api.models.database import DbManager
from datetime import datetime,timedelta
from flask_jwt_extended import(JWTManager,jwt_required,create_access_token,get_jwt_identity)



app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'rhytahz'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] =False
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
    if len(name)<5:
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
    
    username=user_data['username']
    password=user_data['password']
    dbmanager_query=dbmanager.get_by_argument('users','username',username)
    #user=User(dbmanager_query[0], dbmanager_query[1], dbmanager_query[2], dbmanager_query[3])
    
    
    if not username:
        return jsonify({"msg" : "Provide Valid Username"}),400

    if not password:
        return jsonify({"msg" : "Incorrect password"}),400

    if username !='test' or password !='test':
        return jsonify({"msg": "Invalid username or password"})

    access_token= create_access_token(identity=username)
    return jsonify(access_token=access_token),200

@app.route('/api/v2/protected', methods =['GET'])
@jwt_required
def protected():
    #access the identity of current user
    current_user=get_jwt_identity()
    return jsonify(loggesd_in_as=current_user),200
    
    

@app.route('/api/v2/questions', methods =['GET'])
@jwt_required
def fetch_questions():
    current_user=get_jwt_identity()

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
    current_user=get_jwt_identity()
    asked_by =current_user
    request_data=request.get_json()
    subject=request_data['subject']
    #asked_by=request_data['asked_by']
    question= dbmanager.addon_question(subject,asked_by)
    if len(subject)<=2:
        return jsonify({"messagse":'Please write a meaningful question'})
    
    
    return jsonify({
        'message':'Your question has been posted'})


@app.route('/api/v2/questions/<int:question_id>', methods=['GET'])
@jwt_required
def fetch_a_question(question_id):
    current_user=get_jwt_identity()
    question=dbmanager.get_a_question(question_id)
    return jsonify({'Question':question})

@app.route('/api/v2/questions/<int:question_id>', methods=['DELETE'])
@jwt_required
def delete_question(question_id):
    current_user=get_jwt_identity()
    dbmanager.delete_a_question(question_id,current_user)


    return jsonify({'message': 'question {} deleted'.format(question_id)})
    

@app.route('/api/v2/questions/<int:question_id>/answers', methods=['POST'])
@jwt_required
def add_answer_to_question(question_id):
    current_user=get_jwt_identity()
    #answered_by=current_user
    answer_data=request.get_json()
    description=answer_data['description']
    
    if len(description)<=5:
        return jsonify({"message":'Please write a full answer'})

    answer=dbmanager.q_a(question_id,description)
    return jsonify({
        "message":'Answer added for question {}.format(question_id)',
        "answer":answer})

@app.route('/api/v2/questions/<int:question_is>/answers/<int:answer_id', methods=['PUT'])
def prefer():
        data = api.payload
        question_id = question_id
        anwser_id = answer_id
        print(anwser_id)
        accept_status = data['accept_status']
        dbmanager.pacmds(mark, question_id)
        return {'message': 'Answer status updated'}, 201
    

if __name__ == '__main__':
    app.run(debug=True)
  
    
