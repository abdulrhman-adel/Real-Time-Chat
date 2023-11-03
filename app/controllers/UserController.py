from flask import redirect, url_for, render_template, flash, session
from app.models.User import User
from app import db

def LoginController(form):
    username = form.username.data
    password = form.password.data

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(user, password):
        # Authentication succeeded, return a redirect response
        session['user_id'] = user.id
        return redirect(url_for('index'))
    else:
        # Authentication failed, return a rendered template with an error message
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
    return redirect(url_for('index'))

