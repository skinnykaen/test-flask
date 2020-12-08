from  flask_login import UserMixin

from base import db, manager


# class Topic(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), unique=True, nullable=False)
   
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(225), nullable=False)

@manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)