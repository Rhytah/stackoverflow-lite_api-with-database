import psycopg2
from pprint import pprint
from .api_models import User, Answer, Question



class DbManager:
    def __init__(self):
        self.conn =psycopg2.connect(dbname="stacko", user="postgres", host="localhost", password="andela", port="5433")
        self.cur=self.conn.cursor()
        #self.conn.autocommit=
        print (self.cur)
    # def connect(self):
    #     try:
    
    #         self.conn =psycopg2.connect("dbname=overflow user=postgres host=localhost password=andela port=5433")
    #         return self.conn
         
    #     except (Exception, psycopg2.DatabaseError) as error:
    #         print(error)
      

    def create_tables(self):
        sql_cmd1="CREATE TABLE IF NOT EXISTS users(user_id SERIAL PRIMARY KEY,name VARCHAR(25) NOT NULL,username VARCHAR(10),password VARCHAR(30))"
        self.cur.execute(sql_cmd1)
        sql_cmd2="CREATE TABLE IF NOT EXISTS questions(question_id SERIAL PRIMARY KEY,subject VARCHAR(255) NOT NULL,asked_by VARCHAR(30) NOT NULL, user_id FOREIGN KEY,question_date DATE)"
        self.cur.execute(sql_cmd2)
            
        sql_cmd3="CREATE TABLE IF NOT EXISTS answers(answer_id SERIAL PRIMARY KEY,question_id VARCHAR (255) NOT NULL,answered_by VARCHAR(30) NOT NULL,description VARCHAR (255) NOT NULL)"
        self.cur.execute(sql_cmd3)
        self.conn.commit()
        #self.conn.close()

        
        
        
        # for i in sql_cmds:
        #     self.cur.execute(i)
        #     print ('Tables created')
        
        # conn.commit()
        # cur.close()
            
       # except (Exception, psycopg2.DatabaseError) as error:
        #    print(error)

    def register_user(self,name,username,password):
    #    password=self.hash_password(password)
        #user =User(name,username,password)
        user_sql= "INSERT INTO users(name,username,password) VALUES ('{}','{}','{}');".format(name, username,password)#RETURNING user_id;")
        self.cur.execute(user_sql)
        self.conn.commit()
        #self.conn.close()



    def get_by_argument(self, table, column_name,argument):
        query = "SELECT * FROM {} WHERE {} = '{}';".format(table, column_name, argument)
        self.cur.execute(query)
        result = self.cur.fetchone()
        return result

    def add_question(self,subject,asked_by,user_id,question_date):
        aq_cmd= "SELECT user_id FROM users WHERE username = '{}'".format(asked_by)
        self.cur.execute(aq_cmd)
        user=self.cur.fectchone()
        question=Question(subject,asked_by,user_id,question_date)

        q_cmd= "INSERT INTO questions(subject,asked_by,user_id) VALUES ('{}','{}',user[0],question.subject,question.asked_by,question.user_id,question.question_date);".format(subject,asked_by,user_id,question_date)
        print(q_cmd)
        self.cur.execute(q_cmd)
        self.conn.commit()
        #conn=None
        # user_id= None

        # try:
        #     conn=psycopg2.connect("dbname=stacko user=postgres host=localhost password=andela port=5433")
        #     conn=self.connect()
        #     cur= conn.cursor()
        #     cur.execute(sql,users(name,username,password))
        #     user_id =cur.fectchone()[0]
        #     conn.commit()
        #     cur.close()
            
        # except (Exception, psycopg2.DatabaseError) as error:
        #     print(error)
        
        

if __name__ =='__main__':
    app.run()
    db.DbManager()
    db.create_tables()
    db.register_user()
    db.add_question()
