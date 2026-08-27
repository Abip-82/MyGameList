from flask import Flask
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

load_dotenv()
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app =  Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    from .models import User
    
    with app.app_context():
        db.create_all()

    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/auth")

    return app

@login_manager.user_loader
def load_user(user_id):
    from .models import User
    return User.query.get(int(user_id))

