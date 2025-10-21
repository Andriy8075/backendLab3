from marshmallow import Schema, fields, validate


class CategorySchema(Schema):
    """Schema for Category model validation and serialization"""
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=255))
    user_id = fields.Int(required=True, validate=validate.Range(min=1))
    # user = fields.Nested('UserSchema', dump_only=True)


class CategoryCreateSchema(Schema):
    """Schema for creating a new category"""
    name = fields.Str(required=True, validate=validate.Length(min=1, max=255))
    user_id = fields.Int(required=True, validate=validate.Range(min=1))
