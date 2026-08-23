from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length , EqualTo

class SignupForm(FlaskForm):
    
    email = StringField("Email", validators=[DataRequired(message="Email is required"), Email(message="Enter a valid email")])
    username = StringField("Username", validators=[DataRequired(message="Username is required"),Length(min=4,max=100,message="Username must be between 4 and 100 characters")])
    password = PasswordField("Password",validators=[DataRequired(message="Enter a password"),Length(min=8,max=100,message="Password must be atleast 8 characters long")])
    password_confirm = PasswordField("Confirm Password", validators=[DataRequired(message="Please retype your password"),EqualTo("password")])
    sign_up = SubmitField("Sign up")