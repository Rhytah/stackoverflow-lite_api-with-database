
import psycopg2
from flask import Flask


from config import app_configuration

app = Flask(__name__)


def create_app(mode):
    app.config.from_pyfile('config.py')
    app.config.from_object(app_configuration[mode])

    return app

if __name__=='__main__':
    app.run()





        



