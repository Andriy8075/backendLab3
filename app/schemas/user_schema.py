from marshmallow import Schema, fields, validate
from app.config.models_validation.user import name_max_length
from app.config.currencies import SUPPORTED_CURRENCIES


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=name_max_length))
    default_currency = fields.Str(required=True, validate=validate.OneOf(SUPPORTED_CURRENCIES))


class UserCreateSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1, max=name_max_length))
    default_currency = fields.Str(required=True, validate=validate.OneOf(SUPPORTED_CURRENCIES))
