from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired,Email,Length,EqualTo
from project.models import User

def check_email(form, field):
    if User.query.filter_by(email=field.data).first():
        raise ValidationError('Your email has already been registered.')

def check_username(form, field):
    if User.query.filter_by(username=field.data).first():
        raise ValidationError('Your username has already been taken.')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message="Username is required.")])
    password = PasswordField('Password', validators=[DataRequired(message="Password is required.")])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message='Email is required.'),Email(message='Enter a valid email.'), check_email])
    username = StringField('Username', validators=[DataRequired(message='Username is required.'), check_username])
    password = PasswordField('Password', validators=[DataRequired(message='Password is required.'), EqualTo('pass_confirm', message='Passwords must match.')])
    pass_confirm = PasswordField('Confirm password', validators=[DataRequired(message='Please enter a confirm password.')])
    submit = SubmitField('Register')
