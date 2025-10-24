from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from app.models.user import User
from app.schemas.user_schema import UserSchema, UserCreateSchema

user_bp = Blueprint('user', __name__)

@user_bp.route('/user', methods=['POST'])
def create_user():
    try:
        schema = UserCreateSchema()
        data = schema.load(request.form)

        user = User.create(data['name'], data['default_currency'])

        user_schema = UserSchema()
        return jsonify({
            'message': 'user created successfully',
            'user': user_schema.dump(user)
        }), 201
        
    except ValidationError as err:
        return jsonify({
            'error': 'Validation error',
            'messages': err.messages
        }), 400

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = User.get_all()
    user_schema = UserSchema(many=True)
    return jsonify(user_schema.dump(users)), 200

@user_bp.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    user = User.get_by_id(id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404

    user_schema = UserSchema()
    return jsonify(user_schema.dump(user)), 200

@user_bp.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    if User.delete(id):
        return jsonify({'message': 'User deleted successfully'}), 200
    else:
        return jsonify({'error': 'User not found'}), 404