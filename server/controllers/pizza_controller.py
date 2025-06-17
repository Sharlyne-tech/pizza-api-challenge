from flask import Blueprint, jsonify
from models.pizza import Pizza
from server.models.pizza import Pizza

pizza_bp = Blueprint('pizzas', __name__)

@pizza_bp.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    result = [pizza.to_dict() for pizza in pizzas]
    return jsonify(result), 200