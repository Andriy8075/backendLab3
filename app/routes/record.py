from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from app.models.record import Record
from app.schemas.record_schema import RecordSchema, RecordCreateSchema

record_bp = Blueprint('record', __name__)

@record_bp.route('/record', methods=['POST'])
def create_record():
    try:
        # Validate input data using Marshmallow
        schema = RecordCreateSchema()
        data = schema.load(request.form)
        
        # Create record
        record = Record.create(data['category_id'], data['sum'], data.get('currency'))
        
        # Serialize response using Marshmallow
        record_schema = RecordSchema()
        return jsonify({
            'message': 'record created successfully',
            'record': record_schema.dump(record)
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

@record_bp.route('/record/<int:id>', methods=['GET'])
def get_record(id):
    try:
        record = Record.get_by_id(id)
        if record is None:
            return jsonify({'error': 'Record not found'}), 404
        
        record_schema = RecordSchema()
        return jsonify(record_schema.dump(record)), 200
    except Exception as e:
        return jsonify({
            'error': 'Internal server error',
            'message': str(e)
        }), 500

@record_bp.route('/record/<int:id>', methods=['DELETE'])
def delete_record(id):
    try:
        if Record.delete(id):
            return jsonify({'message': 'Record deleted successfully'}), 200
        else:
            return jsonify({'error': 'Record not found'}), 404
    except Exception as e:
        return jsonify({
            'error': 'Internal server error',
            'message': str(e)
        }), 500
