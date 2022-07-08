from warshmallow import Schema, fields

class Cheet(Schema):
    name = fields.Str()
    id = fields.Int()
    context = fields.Str()
    desc = fields.Str()
    note = fields.Str()
    tags = fields.List(fields.Str())
