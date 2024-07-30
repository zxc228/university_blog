from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Length, Email, ValidationError
from blog.models import User
from flask import flash

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()  # Добавляем first()
        if user:
            flash("That username is taken. Choose another", 'danger')
            raise ValidationError("That username is taken. Choose another")
        

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()  # Исправляем проверку email
        if user:
            flash("That email is taken. Choose another", 'danger')
            raise ValidationError("That email is taken. Choose another")
        

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember me")
    submit = SubmitField("Log in")
