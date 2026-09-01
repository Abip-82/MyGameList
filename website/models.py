from . import db
from flask_login import UserMixin

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(50), nullable = False , unique=True)
    username = db.Column(db.String(100), nullable=False, unique = True)
    password_hashed = db.Column(db.String(255), nullable=False)

class Game(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(250), nullable = False)
    api_id = db.Column(db.Integer , nullable = False , unique = True)

class Collection(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    status = db.Column(db.String(50), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id") , nullable = False)
    game_id = db.Column(db.Integer, db.ForeignKey("game.id") , nullable = False)