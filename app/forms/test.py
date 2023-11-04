from wtforms import Form, StringField, validators, SubmitField, BooleanField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, EqualTo, Email, Regexp

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Username must consist of only letters, numbers, dots or underscores')])
    password = StringField('Password', validators=[DataRequired(), Length(min=4, max=25)])
    confirm = StringField('Repeat Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    email = StringField('Email', validators=[DataRequired(), Email()])

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Username must consist of only letters, numbers, dots or underscores')])
    password = StringField('Password', validators=[DataRequired(), Length(min=4, max=25)])
    remember = BooleanField('Remember Me')