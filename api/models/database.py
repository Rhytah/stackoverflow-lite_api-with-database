import psycopg2
from pprint import pprint
from .api_models import User, Answer, Question



class DbManager:
    def __init__(self):
        self.conn =psycopg2.connect(dbname="stacko", user="postgres", host="localhost", password="andela", port="5433")
        self.cur=self.conn.cursor()
        
        print (self.cur)
    
    def create_tables(self):
        sql_cmd1="CREATE TABLE IF NOT EXISTS users(user_id SERIAL PRIMARY KEY,name VARCHAR(25) NOT NULL,username VARCHAR(10),password VARCHAR(30))"
        self.cur.execute(sql_cmd1)
        sql_cmd2="CREATE TABLE IF NOT EXISTS questions(question_id SERIAL PRIMARY KEY,subject VARCHAR(255) NOT NULL,asked_by VARCHAR(30) NOT NULL)"
        self.cur.execute(sql_cmd2)
            
        sql_cmd3="CREATE TABLE IF NOT EXISTS answers(answer_id SERIAL PRIMARY KEY,question_id VARCHAR (255) NOT NULL,answered_by VARCHAR(30) NOT NULL,description VARCHAR (255) NOT NULL, mark BOOLEAN)"
        self.cur.execute(sql_cmd3)
        self.conn.commit()


        

    def register_user(self,name,username,password):
    #    password=self.hash_password(password)
        #user =User(name,username,password)
        user_sql= "INSERT INTO users(name,username,password) VALUES ('{}','{}','{}');".format(name, username,password)#RETURNING user_id;")
        self.cur.execute(user_sql)
        self.conn.commit()
        



    def get_by_argument(self, table, column_name,argument):
        query = "SELECT * FROM {} WHERE {} = '{}';".format(table, column_name, argument)
        self.cur.execute(query)
        result = self.cur.fetchone()
        return result

    def addon_question(self,subject,asked_by):
        q_cmd= "INSERT INTO questions(subject,asked_by) VALUES ('{}','{}');".format(subject,asked_by)
        print(q_cmd)
        self.cur.execute(q_cmd)
        self.conn.commit()

    def get_questions(self):
        gaq_cmd ="SELECT question_id,questions FROM questions;"
        self.cur.execute(gaq_cmd)
        rows = self.cur.fetchall()
        self.conn.commit()
        questions =[questions for questions in rows]
        allqn= []
        for value in range(len(questions)):
            question=(
                {'question_id':questions[value][0],
                'question':questions[value][1]})
            allqn.append(question)
        return allqn
        
    def get_a_question(self,question_id):
        gaq_cmd="SELECT subject,asked_by FROM questions WHERE question_id = {};".format(question_id) 
        self.cur.execute(gaq_cmd)
        question=self.cur.fetchone()
        self.conn.commit()
        return question

    def delete_a_question(self,question_id,asked_by):
        del_cmd="DELETE FROM questions WHERE question_id={} AND asked_by ='{}'".format(question_id,asked_by)
        rows_deleted=self.cur.rowcount
        print(rows_deleted)
        self.cur.execute(del_cmd)
        self.conn.commit
        return rows_deleted
     
    def q_a(self,question_id,description):
        try:
            qcmd="SELECT question_id WHERE question_id={}".format(question_id)
            self.cur.execute(qcmd)
            question=self.cur.fetchone()
            question_id=question[0]
            print (question[0])
            
            acmd="INSERT INTO answers(question_id,description) VALUES ({},'{}')".format(question_id,description)
            self.cur.execute(acmd)
            self.cur.commit()
        except (Exception,psycopg2.DatabaseError) as Error:
            raise Error

    def prefer_answer(self,mark,question_id):
        pacmds ="UPDATE answers SET mark={} WHERE question_id-{} ".format(mark,question_id)
        self.cur.execute(pacmds)
        self.conn.commit
        return {'message':"Answer updated statuz"}

 
        
            


        
# if __name__ =='__main__':
#     app.run()
#     db.DbManager()
#     db.create_tables()
#     db.register_user()
#     db.add_question()
#     db.get_questions()
#     db.get_a_question()
#     db.delete_a_question()
