import psycopg2
from pprint import pprint
from .models import User



class DbManager:
    

    def connect(self):
        try:
    
            self.conn = psycopg2.connect("dbname=overflow user=postgres host=localhost password=andela port=5433")
            return self.conn
        
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
      

    def create_tables(self):
        sql_cmds= (
            """
            CREATE TABLE users(
                user_id SERIAL PIMARY KEY,
                name VARCHAR(25) NOT NULL,
                username VARCHAR(10),
                password VARCHAR(30)
            )
            """,
            """
            CREATE TABLE questions(
                question_id SERIAL PRIMARY KEY,
                subject VARCHAR(255) NOT NULL,
                asked_by VARCHAR(30) NOT NULL
            )
            """,
            """ CREATE TABLE answers(
                answer_id SERIAL PRIMARY KEY,
                question_id VARCHAR (255) NOT NULL,
                answered_by VARCHAR(30) NOT NULL,
                description VARCHAR (255) NOT NULL
            )
            """,
            """CREATE TABLE users(
                user_id SERIAL PRIMARY KEY,
                username VARCHAR (255) NOT NULL

            )
            """
        )

    def register(self,name,username,password):
        password=self.hash_password(password)
        user =User(name,username,password)
        sql= "INSERT INTO users(name,username,password) VALUES ('{}','{}','{}).format(user.name, user.username,user.password)
        pprint(sql)
        self.cur.execute(sql)
        return jsonify({'message': 'USer now registered'})


        try:
            conn=self.connect()
            cur= conn.cursor()
            for i in sql_cmds:
                cur.execute(i)
                print ('Tables')
            cur.close()
            conn.commit()
            
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
            

 
 
if __name__ == '__main__':
    db=DbManager()
    db.create_tables()