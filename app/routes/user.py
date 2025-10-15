from flask import Blueprint, jsonify, request
from app.models.user import User

user_bp = Blueprint('user', __name__)

@user_bp.route('/user', methods=['POST'])
def create_user():
    name = request.form.get('name')
    user = User.create(name)
    return jsonify({
        'message': 'user created successfully',
        'name': user.name,
        'id': user.id,
    }), 200

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = User.get_all()
    dictionaries = []
    for user in users:
        dictionaries.append(user.to_dict())

    return jsonify(dictionaries)

@user_bp.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    user = User.get_by_id(id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user)

@user_bp.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    if User.delete(id):
        return jsonify({'message': 'User deleted successfully'}), 200
    else:
        return jsonify({'error': 'User not found'}), 404