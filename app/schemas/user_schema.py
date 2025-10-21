from marshmallow import Schema, fields, validate
from app.config.models.user import name_max_length


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=name_max_length))


class UserCreateSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1, max=name_max_length))


class UserUpdateSchema(Schema):
    name = fields.Str(validate=validate.Length(min=1, max=name_max_length))
