from marshmallow import Schema, fields, validate, validates_schema, ValidationError
from app.config.models_validation.category import name_max_length
from app.models.user import User


class CategorySchema(Schema):
    """Schema for Category model validation and serialization"""
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=name_max_length))
    user_id = fields.Int(required=True, validate=validate.Range(min=1))
    # user = fields.Nested('UserSchema', dump_only=True)


class CategoryCreateSchema(Schema):
    """Schema for creating a new category"""
    name = fields.Str(required=True, validate=validate.Length(min=1, max=name_max_length))
    user_id = fields.Int(required=True, validate=validate.Range(min=1))
    
    @validates_schema
    def validate_user_exists(self, data, **kwargs):
        """Validate that the user with the specified user_id exists"""
        if 'user_id' in data:
            user = User.query.get(data['user_id'])
            if user is None:
                raise ValidationError('User with specified ID does not exist', field_name='user_id')
