from flask import render_template, request, flash, url_for, Blueprint, redirect
from blog.models import User
from flask_login import login_user, current_user, login_required, logout_user
from blog.user.forms import RegistrationForm, LoginForm
from blog import bcrypt, db
import os
import shutil



users = Blueprint('users', __name__)

@users.route('/registration', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        full_path = os.path.join(os.getcwd(), 'blog/static', 'profile_pics', user.username)
        if not os.path.exists(full_path):
            os.mkdir(full_path)
        
        shutil.copy(rf'{os.getcwd()}/blog/static/profile_pics/default.png', full_path)
        flash('Your account has been created', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', form=form, title='Registration', legend='Registration')


@users.route('/login', methods= ["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')

            return redirect(next_page) if next_page else redirect(url_for('main.account'))
        else:
            flash("Unsuccessful authorization. Check your email or password", 'danger')

    return render_template("login.html", title='Authorization', legend='Login', form=form)


