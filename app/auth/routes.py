from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.user_service import UserService
from app.models.user import User
from app.auth.services import AuthService

auth_bp = Blueprint('auth', __name__)

# Register a new user
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"msg": "Username and password are required"}), 400

    user, error = UserService.register_user(username, password)
    if error:
        return jsonify({"msg": error}), 400

    return jsonify({"msg": "User registered successfully"}), 201

# Login and get a JWT
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"msg": "Username and password are required"}), 400

    access_token, error = AuthService.login(username, password)
    if error:
        return jsonify({"msg": error}), 401

    return jsonify(access_token=access_token), 200

# Get all users (protected route)
@auth_bp.route('/users', methods=['GET'])
@jwt_required()
def get_all_users():
    users = UserService.get_all_users()
    user_list = [{"id": user.id, "username": user.username, "role": user.role} for user in users]
    return jsonify(users=user_list), 200

# Get a specific user by ID (protected route)
@auth_bp.route('/users/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    user = UserService.get_user_by_id(user_id)
    if not user:
        return jsonify({"msg": "User not found"}), 404

    return jsonify(user={"id": user.id, "username": user.username, "role": user.role}), 200

# Update a specific user by ID (protected route)
@auth_bp.route('/users/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    data = request.get_json()
    username = data.get('username')
    role = data.get('role')

    user = UserService.update_user(user_id, username, role)
    if not user:
        return jsonify({"msg": "User not found"}), 404

    return jsonify({"msg": "User updated successfully"}), 200

# Delete a specific user by ID (protected route)
@auth_bp.route('/users/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    success = UserService.delete_user(user_id)
    if not success:
        return jsonify({"msg": "User not found"}), 404

    return jsonify({"msg": "User deleted successfully"}), 200

@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    user = User.query.filter_by(username=current_user).first()
    # return jsonify({'message': f'You are accessing a protected route, {current_user}'}), 200
    return jsonify(logged_in_as=current_user, user={"username": user.username, "role": user.role}), 200