from flask import Flask
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()
db = SQLAlchemy()

def create_app():
    app =  Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")
    db.init_app(app)

    from .models import User
    
    with app.app_context():
        db.create_all()

    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/auth")

    return app