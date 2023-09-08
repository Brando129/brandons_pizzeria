from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import models_pizza, models_order

# Post Routes
# Route for creating a pizza.
@app.post('/create_pizza')
def create_pizza():
    if 'user_id' not in session:
        return redirect('/logout')
    if not models_pizza.Pizza.validate_pizza(request.form):
        return redirect('/craft_pizza')
    pizza = {
        'method': request.form['method'],
        'size': request.form['size'],
        'crust': request.form['crust'],
        'quantity': request.form['quantity'],
        'meat': request.form['meat'],
        'cheese': request.form['cheese'],
        'sauce': request.form['sauce'],
        'topping': request.form['topping'],
        'order_id': session['user_id']
    }
    models_pizza.Pizza.save_new_pizza(pizza)

    order = {
        'total': float(12.99),
        'user_id': session['user_id']
    }
    models_order.Order.save_new_order(order)
    return redirect('/homepage')