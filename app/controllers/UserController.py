from flask import redirect, url_for, render_template, flash, session
from app.models.User import User
from app import db, login_manager
from flask_login import login_user, logout_user, current_user


@login_manager.user_loader
def LoadUser(user_id):
    return User.query.get(int(user_id))


def LoginController(form):
    username = form.username.data
    password = form.password.data
    remember = form.remember.data

    user = User.query.filter_by(username=username).first()
    login_user(user, remember=remember)  # Pass user_object to load the user into the session
    if current_user.is_authenticated:
        flash('User logged in successfully', 'success')
        return redirect(url_for('chat'))
    else:
        flash('Invalid credentials', 'error')
        return render_template('login.html', form=form)


def RegisterController(form):
    username = form.username.data
    password = form.password.data
    email = form.email.data

    # Check if the username or email already exists in the database
    existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
    if existing_user:
        flash('Username or email already exists', 'error')
        return render_template('register.html', form=form)

    # Create a new user
    user = User(username=username, email=email)
    user.set_password(password)
    user.save()

    flash('User successfully registered', 'success')
    return redirect(url_for('chat'))
