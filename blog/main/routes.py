from flask import render_template, request, flash, url_for, Blueprint, redirect
from blog.main.forms import LoginForm
from blog.models import User
from flask_login import login_user, current_user, login_required, logout_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html', title='Main')

@main.route('/blog')
def blog():
    return render_template('index.html', title='blog')

# @main.route('/login', methods= ["GET", "POST"])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()
#         if user and user.check_password(form.password.data):
#             login_user(user, remember=form.remember.data)
#             next_page = request.args.get('next')

#             return redirect(next_page) if next_page else redirect(url_for('main.account'))
#         else:
#             flash("Unsuccessful authorization. Check your email or password", 'danger')

#     return render_template("login.html", title='Authorization', legend='Login', form=form)

# @main.route('/account')
# @login_required
# def account():
#     return render_template("account.html", title='Account', current_user=current_user)

# @main.route('/logout')

# def logout():
#     logout_user()
#     return redirect(url_for('main.index'))

@main.route('/first_rule')
def first_rule():
    return render_template('first_rule.html')

@main.route('/second_rule')
def second_rule():
    return render_template('second_rule.html')

@main.route('/third_rule')
def third_rule():
    return render_template('third_rule.html')

@main.route('/fourth_rule')
def fourth_rule():
    return render_template('fourth_rule.html')

@main.route('/fifth_rule')
def fifth_rule():
    return render_template('fifth_rule.html')

@main.route('/sixth_rule')
def sixth_rule():
    return render_template('sixth_rule.html')
