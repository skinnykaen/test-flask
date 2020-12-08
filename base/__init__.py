from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.secret_key = '123'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:123@localhost/py_base'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
manager = LoginManager(app)

from base import models, routes

# if __name__ == '__main__':
#     app.run() 'postgres://postgres:123@localhost/py_base'
# app.debug = True

db.create_all()