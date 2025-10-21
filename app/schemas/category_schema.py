from marshmallow import Schema, fields, validate
from app.config.models_validation.category import name_max_length


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
