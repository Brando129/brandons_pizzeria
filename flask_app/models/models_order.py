from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import models_user

# Database name
db = "brandons_pizzeria"

# Order class.
class Order:
    def __init__(self, data):
        self.id = data['id']
        self.total = data['total']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    # Classmethod for saving a new order
    @classmethod
    def save_new_order(cls, data):
        query = """INSERT INTO orders (total, user_id)
                VALUES (%(total)s, %(user_id)s);"""
        return connectToMySQL(db).query_db(query, data)