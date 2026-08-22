from flask import Blueprint

auth = Blueprint("auth",__name__)

@auth.route("/login")
def login():
    return render_template("login.html")

@auth.route("/signup")
def signup():
    return render_template("signup.html")
