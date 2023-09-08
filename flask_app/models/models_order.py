from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import models_user

# Database name
db = "brandons_pizzeria"

# Order class.
class Order:
    def __init__(self, data):
        self.id = data['id']
        self.total = data['total']
        self.method = data['method']
        self.size = data['size']
        self.crust = data['crust']
        self.quantity = data['quantity']
        self.meat = data['meat']
        self.cheese = data['cheese']
        self.sauce = data['sauce']
        self.topping = data['topping']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    # Classmethod for saving a new order
    @classmethod
    def save_new_order(cls, data):
        query = """INSERT INTO orders (total, method, size, crust, quantity, meat, cheese, sauce, topping, user_id)
                VALUES (%(total)s, %(method)s, %(size)s, %(crust)s, %(quantity)s, %(meat)s, %(cheese)s, %(sauce)s, %(topping)s, %(user_id)s);"""
        return connectToMySQL(db).query_db(query, data)

    # Classmethod for getting all the orders for a specific user.
    @classmethod
    def get_all_user_orders(cls):
        query = """SELECT * FROM orders JOIN users on
                users.id = orders.user_id WHERE user_id = %(id)s;"""
        results = connectToMySQL(db).query_db(query)
        customer_orders = []
        for row in results:
            order = cls(row)
            each_order = {
                'id': row['pizzas.id'],
                'method': row['method'],
                'size': row['size'],
                'crust': row['crust'],
                'quantity': row['quantity'],
                'meat': row['meat'],
                'cheese': row['cheese'],
                'sauce': row['sauce'],
                'topping': row['topping'],
                'user_id': row['user_id'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            }
            order.user = models_user.User(each_order)
            customer_orders.append(order)
        return customer_orders