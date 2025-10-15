from flask import Blueprint, jsonify, request
from app.models.record import Record

record_bp = Blueprint('record', __name__)

@record_bp.route('/record', methods=['POST'])
def create_record():
    sum = request.form.get('sum')
    user_id = request.form.get('user_id')
    category_id = request.form.get('category_id')
    record = Record.create(user_id, category_id, sum)
    return jsonify({
        'message': 'record created successfully',
        'sum': record.sum,
        'id': record.id,
        'category_id': record.category_id,
        'user_id': record.user_id,
        'date_time': record.date_time
    }), 200

@record_bp.route('/record/<int:id>', methods=['GET'])
def get_record(id):
    record = Record.get_by_id(id)
    if record is None:
        return jsonify({'error': 'Record not found'}), 404
    return jsonify(record)

@record_bp.route('/record/<int:id>', methods=['DELETE'])
def delete_record(id):
    if Record.delete(id):
        return jsonify({'message': 'Record deleted successfully'}), 200
    else:
        return jsonify({'error': 'Record not found'}), 404
