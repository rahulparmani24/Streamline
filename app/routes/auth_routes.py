# User authentication endpoints
from flask import Blueprint, request, jsonify

auth_bp = Blueprint('auth', __name__)

# Placeholder for user database
users = {}

@auth_bp.route('/signup', methods=['POST'])
def signup():
    """
    Endpoint for user sign-up.
    """
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username in users:
        return jsonify({'message': 'User already exists'}), 400

    users[username] = password
    return jsonify({'message': 'User signed up successfully'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Endpoint for user login.
    """
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username not in users or users[username] != password:
        return jsonify({'message': 'Invalid credentials'}), 401

    return jsonify({'message': 'Login successful'}), 200
