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
@app.route('/login')
def login():
    return render_template('login.html')