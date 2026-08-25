from flask import Blueprint , render_template , redirect, url_for
from .forms import SignupForm , LoginForm
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint("auth",__name__)

@auth.route("/login", methods = ['GET','POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password_hashed, password):
            return(redirect(url_for("views.home")))
        else:
            form.form_errors = ["Invalid email or password"]
    return render_template("login.html", form=form)

@auth.route("/signup", methods = ['GET', 'POST'])
def signup():
    
    form = SignupForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        username = form.username.data
        password_hashed = generate_password_hash(password)

        user = User(email=email,username=username,password_hashed=password_hashed)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("auth.login"))

    return render_template("signup.html", form=form)



