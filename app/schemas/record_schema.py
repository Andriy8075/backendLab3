from marshmallow import Schema, fields, validate
from datetime import datetime


class RecordSchema(Schema):
    """Schema for Record model validation and serialization"""
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True, validate=validate.Range(min=1))
    category_id = fields.Int(required=True, validate=validate.Range(min=1))
    sum = fields.Float(required=True, validate=validate.Range(min=0.01))
    date_time = fields.DateTime(dump_only=True)
    # user = fields.Nested('UserSchema', dump_only=True)
    # category = fields.Nested('CategorySchema', dump_only=True)


class RecordCreateSchema(Schema):
    """Schema for creating a new record"""
    user_id = fields.Int(required=True, validate=validate.Range(min=1))
    category_id = fields.Int(required=True, validate=validate.Range(min=1))
    sum = fields.Float(required=True, validate=validate.Range(min=0.01))
    date_time = fields.DateTime(load_default=datetime.utcnow, allow_none=True)
