from flask import Blueprint, jsonify, request
from models.restaurant import Restaurant
from models.restaurant_pizza import RestaurantPizza
from server.models.restaurant import Restaurant
from server.models.restaurant_pizza import RestaurantPizza
from server.app import db

restaurant_bp = Blueprint('restaurants', __name__)
     @@ -17,14 +17,14 @@
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    return jsonify(restaurant.to_dict(include_pizzas=True)), 200
    return jsonify(restaurant.to_dict()), 200

@restaurant_bp.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    db.session.delete(restaurant)
    db.session.commit()
    return '', 204