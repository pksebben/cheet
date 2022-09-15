import json
import tempfile
import subprocess
from uuid import uuid4
from marshmallow import Schema, fields, post_load
from marshmallow.exceptions import ValidationError

# import cheet_compile
import random

class DefaultList(fields.List):
    def _deserialize(self, value, attr, data, **kwargs):
        value = value or []
        print(f"deserializing : {value}")
        return super()._deserialize(value, attr, data, **kwargs)

    def _serialize(self, value, attr, obj, **kwargs):
        value = value or []
        print(f"serializing : {value}")
        return super()._serialize(value, attr, obj, **kwargs)

class CheetSchema(Schema):
    name = fields.Str()
    id = fields.Str(default=str(uuid4()))
    key = fields.Str()
    context = fields.Str()
    description = fields.Str()
    note = fields.Str(allow_none=True)
    tags = DefaultList(fields.Str(), allow_none=True)

    @post_load
    def make_cheet(self, data, **kwargs):
        try:
            return Cheet(**data)
        except Exception as e:
            print(f"failed to make cheet: {data}\n{e}")


class Cheet:
    # statics
    schema = CheetSchema()

    # constructors
    @classmethod
    def load_file(self, path):
        """load a set of cheets from a json file"""
        try:
            with open(path, "r") as f:
                return self.schema.loads(f.read(), many=True)
        except ValidationError as e:
            raise ValidationError(f"Validation error for {path}: {e}")

    @classmethod
    def from_dict(self, cdict):
        print(cdict)
        cheet = self.schema.load(cdict)
        # required = ['name', 'key', 'context', 'description']
        # for k in required:
        #     if k not in cdict.keys():
        #         raise ValidationError(f"missing key: {k}")

        # cheet = Cheet(
        #     cdict.get('name'),
        #     cdict.get('key'),
        #     cdict.get('context'),
        #     cdict.get('description'),
        #     cdict.get('note'),
        #     cdict.get('tags') or [],
        #     cdict.get('id')
        # )
        return cheet

    def __init__(self,
                 name,
                 key,
                 context,
                 description,
                 note = None,
                 tags = [],
                 id = None):
        self.name = name
        self.key = key
        self.context = context
        self.description = description
        self.note = note
        if tags is not None:
            self.tags = tags
        else:
            self.tags = []
        if id is not None:
            self.id = id
        else:
            self.id = str(uuid4())

    def __eq__(self, other):
        return all([
            self.name == other.name,
            self.key == other.key,
            self.context == other.context,
            self.description == other.description,
            self.note == other.note,
            self.tags == other.tags,
            self.id == other.id
        ])

    def vim_edit(self):
        """edit this cheet using a vim subprocess"""
        # TODO: accept cheet and return it as json?
        # TODO: cheet validation

        c = Cheet.schema.dumps(self, indent=2)

        with tempfile.NamedTemporaryFile(suffix='temp') as temp:
            with open(temp.name, "w") as t:
                t.write(c)
            subprocess.call(['/usr/bin/vim', temp.name])
            text = open(temp.name, 'r').read()
            return Cheet.schema.loads(text)

    def pprint(self):
        print(self.schema.dumps(self, indent=3))
