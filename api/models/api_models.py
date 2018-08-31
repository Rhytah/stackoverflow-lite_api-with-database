import psycopg2
import os
class User:
    def __init__(self,user_id,name,username,password):
        self.user_id=user_id
        self.name=name
        self.username=username
        self.password =password
    
users=[]



class Question:
    def __init__(self,question_id,subject,asked_by):
        self.question_id = question_id
        self.subject = subject
        self.asked_by =asked_by
        
        

questions=[]

class Answer:
    def __init__(self, answer_id,question_id, answered_by,description):
        self.answer_id= answer_id
        self.question_id = question_id
        self.answered_by = answered_by
        self.description=description
answers=[]


# if __name__=='__main__':
#     app.run()

