from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired,Email,Length,EqualTo
from project.models import User

def testingboi(form, field):
    if field.data < 10:
        raise ValidationError('Must be 42')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message="Username is required.")])
    password = PasswordField('Password', validators=[DataRequired(message="Password is required.")])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message='Email is required.'),Email(message='Enter a valid email.')])
    username = StringField('Username', validators=[DataRequired(message='Username is required.')])
    password = PasswordField('Password', validators=[DataRequired(message='Password is required.'), EqualTo('pass_confirm', message='Passwords must match.')])
    pass_confirm = PasswordField('Confirm password', validators=[DataRequired(message='Please enter a confirm password.')])
    submit = SubmitField('Register')
'''
    def check_email(self, field):
        # Check if not None for that user email!
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')

    def check_username(self, field):
        # Check if not None for that username!
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Sorry, that username is taken!')
            '''
