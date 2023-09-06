from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import models_user, models_pizza
# Bcrypt import
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app) # We are creating an object called bcrypt,
# which is made by invoking the function Bcrypt with our app as an argument.

# Get Routes
# Route for rendering the Registration page.
@app.route('/')
def registration():
    return render_template('registration.html')

# Route for rendering the Login page.
@app.route('/user_login')
def user_login():
    return render_template('login.html')

# Route for logging a user out.
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/user_login')

# Route for rendering the Homepage.
@app.route('/homepage')
def check_session():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': session ['user_id']
    }
    return render_template('homepage.html')

# Post Routes
# Route for registering a user.
@app.post('/register')
def register():
    return redirect('/homepage')

# Route for logging a user in.
@app.post('/login')
def login():
    return redirect('/homepage')