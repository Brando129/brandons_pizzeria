from flask_app.config.mysqlconnection import connectToMySQL

# Database name
db = "brandons_pizzeria"

# Favorite class.
class Favorite:
    def __init__(self, data):
        self.id = data['id']
        self.size = data['size']
        self.crust = data['crust']
        self.meat = data['meat']
        self.cheese = data['cheese']
        self.sauce = data['sauce']
        self.topping = data['topping']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Classmethod for saving a new favorite.
    @classmethod
    def save_new_favorite(cls, data):
        query = """INSERT INTO favorites (size, crust, meat, cheese, sauce, topping, user_id)
                VALUES (%(size)s, %(crust)s, %(meat)s, %(cheese)s, %(sauce)s, %(topping)s, %(user_id)s);"""
        return connectToMySQL(db).query_db(query, data)

    # Classmethod for getting all the orders from a specific user.
    @classmethod
    def get_user_favortie(cls, data):
        query = """SELECT * FROM favorites WHERE favorites.id = 1 AND user_id = %(id)s;""" # This query needs
        results = connectToMySQL(db).query_db(query, data)
        print(results)
        customer_favorite = []
        for favorite in results:
            print(favorite)
            customer_favorite.append(cls(favorite))
        return customer_favorite