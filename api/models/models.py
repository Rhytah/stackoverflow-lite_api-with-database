import psycopg2
import os
import database_config

database_config

class User:
    def __init__(self,user_id,name,username,email,password):
        self.user_id=user_id
        self.name=name
        self.username=username
        self.password =password

users=[]



class Question:
    def __init__(self,question_id,subject,asked_by,question_date):
        self.question_id = question_id
        self.subject = subject
        self.asked_by =asked_by

questions=[]

class Answer:
    def __init__(self, answer_id,question_id, answered_by,description,answer_date):
        self.answer_id= answer_id
        self.question_id = question_id
        self.answered_by = answered_by
        self.description=description
answers=[]




