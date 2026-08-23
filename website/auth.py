from flask import Blueprint , render_template , redirect, url_for
from .forms import SignupForm

auth = Blueprint("auth",__name__)

@auth.route("/login", methods = ['GET','POST'])
def login():
    return render_template("login.html")

@auth.route("/signup", methods = ['GET', 'POST'])
def signup():
    
    form = SignupForm()

    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password = form.password.data
        password_confirm = form.password_confirm.data
 
        return redirect(url_for("auth.login"))

    return render_template("signup.html", form=form)

