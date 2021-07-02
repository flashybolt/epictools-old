from project import app,db,templates
from flask import render_template, redirect, request, url_for, flash,abort
from flask_login import login_user,login_required,logout_user
from project.models import User
from project.forms import LoginForm, RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/')
def home():
    return render_template('home.html', title="Home | Epictools")


@app.route('/tools', methods=['GET', 'POST'])
@login_required
def tools():
    return render_template('tools.html', title="tools | Epictools")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You logged out!')
    return redirect(url_for('home'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Grab the user from our User Models table
        user = User.query.filter_by(username=form.username.data).first()
        print(user)
        be_banana()

        # Check that the user was supplied and the password is right
        # The verify_password method comes from the User object
        # https://stackoverflow.com/questions/2209755/python-operation-vs-is-not

        if user.check_password(form.password.data) and user is not None:
            #Log in the user
            login_user(user)
            flash('Logged in successfully.')
            # If a user was trying to visit a page that requires a login
            # flask saves that URL as 'next'.
            #next = request.args.get('next')
            #print(next)
            # So let's now check if that next exists, otherwise we'll go to
            # the welcome page.
            #if next == None or not next[0]=='/':
            #    next = url_for('tools')
            #return redirect(next)
        elif user is None:
            flash('User does not exist.')
    return render_template('login.html', title="Login", form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        usernameexists = User.query.filter_by(username=user.username).first() is not None
        emailexists = User.query.filter_by(email=user.email).first() is not None

        if usernameexists or emailexists:
            flash('Username or email has already been registered.')
        else:
            db.session.add(user)
            db.session.commit()
            flash('Thanks for registering! Now you can login!')
            return redirect(url_for('login'))
    return render_template('register.html', title="Register", form=form)

if __name__ == '__main__':
    app.run(debug=True)
