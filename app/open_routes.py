from flask import Blueprint, jsonify

# Create a Blueprint for open routes
open_bp = Blueprint('open', __name__)

@open_bp.route('/welcome', methods=['GET'])
def welcome():
    return jsonify({"message": "Welcome to the open route!"}), 200