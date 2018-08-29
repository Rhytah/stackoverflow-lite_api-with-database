from flask_restful import Resource
from flask import request, api

from models import Question, Answer, User
from .app import api
from api.database_config import DbManager

app=Flask(__name__)


dbmanager= DbManager(host='localhost', database='overflow',user='postgres',password='andela')

class Signup(Resource):
    def post(self):
        user_data =request.get_json()
        name=user_data['name']
        username=user_data['username']
        password=user_data['password']

        if not user_data:
            return {'message':'All fields are required'}

        if not username or username=" ":
            return {'message':'Please enter a valid UserName'}

    

