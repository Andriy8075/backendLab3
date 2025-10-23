from marshmallow import Schema, fields, validate, validates_schema, ValidationError
from datetime import datetime
from app.config.models_validation.record import min_sum
from app.models.user import User
from app.models.category import Category


class RecordSchema(Schema):
    """Schema for Record model validation and serialization"""
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True, validate=validate.Range(min=1))
    category_id = fields.Int(required=True, validate=validate.Range(min=1))
    sum = fields.Int(required=True, validate=validate.Range(min=min_sum))
    date_time = fields.DateTime(dump_only=True)
    # user = fields.Nested('UserSchema', dump_only=True)
    # category = fields.Nested('CategorySchema', dump_only=True)


class RecordCreateSchema(Schema):
    """Schema for creating a new record"""
    user_id = fields.Int(required=True, validate=validate.Range(min=1))
    category_id = fields.Int(required=True, validate=validate.Range(min=1))
    sum = fields.Int(required=True, validate=validate.Range(min=min_sum))
    date_time = fields.DateTime(load_default=datetime.utcnow, allow_none=True)
    
    @validates_schema
    def validate_user_and_category_exist(self, data, **kwargs):
        """Validate that both user and category with specified IDs exist"""
        # Check if user exists
        if 'user_id' in data:
            user = User.query.get(data['user_id'])
            if user is None:
                raise ValidationError('User with specified ID does not exist', field_name='user_id')
        
        # Check if category exists
        if 'category_id' in data:
            category = Category.query.get(data['category_id'])
            if category is None:
                raise ValidationError('Category with specified ID does not exist', field_name='category_id')
