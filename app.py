from project import app,db,templates
from flask import render_template, redirect, request, url_for, flash, abort
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
    return render_template('tools.html', title="Tools | Epictools")

@app.route('/workshop', methods=['GET', 'POST'])
@login_required
def workshop():
    return render_template('workshop.html', title="Workshop | Epictools")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You logged out!', 'modal')
    return redirect(url_for('home'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        try:
            if user.check_password(form.password.data) and user is not None:
                login_user(user)
                flash('Logged in successfully.', 'modal')
                next = request.args.get('next')
                if next == None or not next[0]=='/':
                    next = url_for('home')
                return redirect(next)
            elif not user.check_password(form.password.data):
                flash('Your password is incorrect.', 'form')
                return redirect(url_for('login'))
        except AttributeError:
            if user is None:
                flash('User does not exist.', 'form')
                return redirect(url_for('login'))
    return render_template('login.html', title="Login", form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering! Now you can login!', 'modal')
        return redirect(url_for('login'))
    return render_template('register.html', title="Register", form=form)

if __name__ == '__main__':
    app.run(debug=True)
