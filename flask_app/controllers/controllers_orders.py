from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import models_order

# Post Routes
# Route for creating a order.
@app.post('/create_order')
def create_order():
    if 'user_id' not in session:
        return redirect('/logout')
    order = {
        'total': session['total'],
        'user_id': session['user_id']
    }
    models_order.Order.save_new_order(order)
    return redirect('/homepage')