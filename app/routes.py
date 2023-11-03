from app import app
from flask import render_template
from app.forms.test import RegistrationForm, LoginForm
from app.controllers.UserController import RegisterController, LoginController


@app.route('/', methods=['GET', 'POST'])
def index():
   return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        response = RegisterController(form)
        return response

    return  render_template("register.html", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        response = LoginController(form)
        return response
    return  render_template("login.html", form=form)
