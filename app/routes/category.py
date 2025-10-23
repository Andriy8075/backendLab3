from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from app.models.category import Category
from app.schemas.category_schema import CategorySchema, CategoryCreateSchema

category_bp = Blueprint('category', __name__)

@category_bp.route('/category', methods=['POST'])
def create_category():
    try:
        schema = CategoryCreateSchema()
        data = schema.load(request.form)

        category = Category.create(data['name'], data['user_id'])

        category_schema = CategorySchema()
        return jsonify({
            'message': 'category created successfully',
            'category': category_schema.dump(category)
        }), 201
        
    except ValidationError as err:
        return jsonify({
            'error': 'Validation error',
            'messages': err.messages
        }), 400
    except Exception as e:
        return jsonify({
            'error': 'Internal server error',
            'message': str(e)
        }), 500

@category_bp.route('/category', methods=['GET'])
def get_categories():
    try:
        categories = Category.get_all()
        category_schema = CategorySchema(many=True)
        return jsonify(category_schema.dump(categories)), 200
    except Exception as e:
        return jsonify({
            'error': 'Internal server error',
            'message': str(e)
        }), 500

@category_bp.route('/category/<int:id>', methods=['DELETE'])
def delete_category(id):
    try:
        if Category.delete(id):
            return jsonify({'message': 'Category deleted successfully'}), 200
        else:
            return jsonify({'error': 'Category not found'}), 404
    except Exception as e:
        return jsonify({
            'error': 'Internal server error',
            'message': str(e)
        }), 500