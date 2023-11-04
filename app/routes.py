from app import app
from flask import render_template, redirect, url_for, flash
from app.forms.test import RegistrationForm, LoginForm
from app.controllers.UserController import RegisterController, LoginController
from app.controllers.GroupController import GroupController
from flask_login import login_required, logout_user, current_user



@app.route('/', methods=['GET', 'POST'])
def index():
    # if user is not logged in, redirect to login page else redirect to chat page
    if not current_user.is_authenticated:
        flash('Please login to continue', 'error')
        return redirect(url_for('login'))
    else:
        return redirect(url_for('chat'))



@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        flash('User already logged in', 'error')
        return redirect(url_for('chat'))
    else:
        form = RegistrationForm()
        if form.validate_on_submit():
            response = RegisterController(form)
            return response

        return render_template("register.html", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('User already logged in', 'error')
        return redirect(url_for('chat'))
    else:
        form = LoginForm()
        if form.validate_on_submit():
            response = LoginController(form)
            return response
        return render_template("login.html", form=form)


@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    flash('User logged out successfully', 'success')
    return redirect(url_for('login'))


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if not current_user.is_authenticated:
        flash('Please login to continue', 'error')
        return redirect(url_for('login'))
    else:
        username = current_user.username
        rooms = GroupController.get_groups_names()
        return render_template("chat.html", username=username, rooms=rooms)

#
# @app.route('/test', methods=['GET', 'POST'])
# def tst():
#     username = current_user.username
#     rooms = GroupController.get_groups_names()
#
#     return render_template("chat.html", username=username, rooms=rooms)
#
