from flask import Blueprint, jsonify, request
from app.models.category import Category

category_bp = Blueprint('category', __name__)

@category_bp.route('/category', methods=['POST'])
def create_category():
    name = request.form.get('name')
    category = Category.create(name)
    return jsonify({
        'message': 'user created successfully',
        'name': category.name,
        'id': category.id,
    }), 200

@category_bp.route('/category', methods=['GET'])
def get_categories():
    categories = Category.get_all()
    dictionaries = []
    for category in categories:
        dictionaries.append(category.to_dict())

    return jsonify(dictionaries)

@category_bp.route('/category/<int:id>', methods=['DELETE'])
def delete_category(id):
    if Category.delete(id):
        return jsonify({'message': 'User deleted successfully'}), 200
    else:
        return jsonify({'error': 'User not found'}), 404