from . import db
from flask_login import UserMixin

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(50), nullable = False)
    username = db.Column(db.String(100), nullable=False, unique = True)
    password_hashed = db.Column(db.String(255), nullable=False)
