from flask_app.config.mysqlconnection import connectToMySQL
# Flash messages import
from flask import flash
from flask_app.models import models_user

# Database name
db = "brandons_pizzeria"

# Pizza class.
class Pizza:
    def __init__(self, data):
        self.id = data['id']
        self.method = data['method']
        self.size = data['size']
        self.crust = data['crust']
        self.quantity = data['quantity']
        self.meat = data['meat']
        self.cheese = data['cheese']
        self.sauce = data['sauce']
        self.topping = data['topping']
        self.order_id = data['order_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Classmethod for saving a new pizza.
    @classmethod
    def save_new_pizza(cls, data):
        query = """INSERT INTO pizzas (method, size, crust, quantity, meat, cheese, sauce, topping, order_id)
                VALUES (%(method)s, %(size)s, %(crust)s, %(quantity)s, %(meat)s, %(cheese)s, %(sauce)s, %(topping)s, %(order_id)s);"""
        return connectToMySQL(db).query_db(query, data)

    # Classmethod for getting all the pizzas for a specific user.
    # @classmethod
    # def get_all_customer_pizzas(cls):
    #     query = """SELECT * FROM pizzas JOIN users on
    #             users.id = pizzas.user_id WHERE user_id = %(id)s;"""
    #     results = connectToMySQL(db).query_db(query)
    #     customer_pizzas = []
    #     for row in results:
    #         pizza = cls(row)
    #         each_pizza = {
    #             'id': row['pizzas.id'],
    #             'method': row['method'],
    #             'size': row['size'],
    #             'crust': row['crust'],
    #             'quantity': row['quantity'],
    #             'meat': row['meat'],
    #             'cheese': row['cheese'],
    #             'sauce': row['sauce'],
    #             'topping': row['topping'],
    #             'user_id': row['user_id'],
    #             'created_at': row['created_at'],
    #             'updated_at': row['updated_at']
    #         }
    #         pizza.user = models_user.User(each_pizza)
    #         customer_pizzas.append(pizza)
    #     return customer_pizzas

    # Classmethod for getting a pizza by it's ID.
    @classmethod
    def get_pizza_by_id(cls, data):
        query = "SELECT * FROM pizzas WHERE id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        return cls(results[0])

    # Classmethod for getting a deleting a pizza.
    @classmethod
    def destroy_pizza(cls, data):
        query = "Delete * FROM pizzas WHERE id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        return cls(results[0])

    # Staticmethod for validating a pizza.
    @staticmethod
    def validate_pizza(data):
        # Set is_valid to True.
        is_valid = True
        # Test if the method is selected.
        if data['method'] == '':
            flash("Method is required", "pizza")
            is_valid = False
        # Test if size is selected.
        if data['size'] == '':
            flash("Size is required.", "pizza")
            is_valid = False
        # Test if crust is selected.
        if data['crust'] == '':
            flash("Crust is required.", "pizza")
            is_valid = False
        # Test if quantity is selected.
        if data['quantity'] == '':
            flash("Quantity is required.", "pizza")
            is_valid = False
        # Test if quantity is selected.
        if data['sauce'] == '':
            flash("Sauce is required.", "pizza")
            is_valid = False
        # Test if quantity is selected.
        if data['cheese'] == '':
            flash("Cheese is required.", "pizza")
            is_valid = False
        return is_valid