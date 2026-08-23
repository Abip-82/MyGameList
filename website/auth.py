from flask import Blueprint , render_template 
import request

auth = Blueprint("auth",__name__)

@auth.route("/login", methods = ['GET','POST'])
def login():
    return render_template("login.html")

@auth.route("/signup", methods = ['GET', 'POST'])
def signup():
    email = request.form.get("email")
    username=request.form.get("username")
    password = request.form.get("password")
    password_confirm =  request.form.get("password_confirm")
    return render_template("signup.html")
