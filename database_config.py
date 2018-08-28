import psycopg2
#from app import db

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
            CREATE TABLE questions(
                question_id SERIAL PRIMARY KEY,
                question_title VARCHAR(255) NOT NULL
            )
            """,
            """ CREATE TABLE answers(
                answer_id SERIAL PRIMARY KEY,
                answer_detail VARCHAR (255) NOT NULL
            )
            """,
            """CREATE TABLE users(
                user_id SERIAL PRIMARY KEY,
                username VARCHAR (255) NOT NULL

            )
            """
        )

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