from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse
from flask_website import flask_website
from flask_website.forms import LoginForm
from flask_website.models import User
from flask_website.forms import RegistrationForm
from flask_website import db

@flask_website.route('/')
@flask_website.route('/index')
@login_required
def index():
    posts = [
        {
            'author': {'username': 'Bot'},
            'body': 'Highly recommend'
        },
        {
            'author': {'username': 'Chi'},
            'body': 'The best restaurant i have ever seen!!'
        }
    ]
    return render_template('index.html', title='Home', posts=posts)


@flask_website.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@flask_website.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@flask_website.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you successfully registered!!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

