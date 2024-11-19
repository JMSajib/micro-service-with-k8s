from flask import Blueprint, request, jsonify

auth_blueprint = Blueprint('auth', __name__)

# A simple in-memory user store for demonstration purposes
users = {}

@auth_blueprint.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    if username in users:
        return jsonify({'error': 'User already exists'}), 400

    users[username] = password
    return jsonify({'message': 'User registered successfully'}), 201


@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    if users.get(username) != password:
        return jsonify({'error': 'Invalid credentials'}), 401

    return jsonify({'message': f'Welcome, {username}!'}), 200

@auth_blueprint.route('/alive', methods=['GET'])
def alive():
    print(f"********** I AM ALIVE ***********")
    return jsonify({'message': f'Auth Alive'}), 200
