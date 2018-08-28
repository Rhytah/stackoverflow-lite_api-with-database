import psycopg2
from app import db

class User:
    def __init__(self,user_id,name,username,email,password)
    self.user_id=user_id
    self.name=name
    self.username=username
    self.email=email
    self.password =password

class Question:
    def __init__(self,question_id,subject,asked_by,question_date):
        self.question_id = question_id
        self.subject = subject
        self.asked_by =asked_by
        self.question_date = question_date

class Answer:
    def __init__(self, answer_id,question_id, answered_by,description,answer_date):
        self.answer_id= answer_id
        self.question_id = question_id
        self.answered_by = answered_by
        self.description=description
        self.answer_date=answer_date


