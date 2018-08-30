import os
from app import create_app
#from api.models.database import DbManager
from api.views import *

# dbmanager=DbManager()
#hashed_password=dbmanager.hash_password()
# app = create_app("development")
# dbmanager.create_tables()
# dbmanager.register_user('name','username','password')


if __name__=='__main__':
    app.run(debug=True)
    
