import json

class CheetSheet:
    """A set of cheets."""
    def __init__(self, cheets = []):
        self.cheets = cheets

    @classmethod
    def from_json(cls, cheets_as_json: [str]) -> 'CheetSheet':
        cheets = json.loads(cheets_as_json)
        cheetlist = []
        for cheet in cheets:
            cheetlist.append(Cheet.from_json(cheet))
        return cls(cheets = cheetlist)

    def as_json(self):
        # TODO: implement
        pass

    def reduce_by_tag(self, tag: str):
        self.cheets = list(filter(lambda x: tag in x.tags, self.cheets))

class Cheet:
    """
    A single cheatsheet entry

    This class handles conversion to and from other representations of a cheet,
    as well as changes to the underlying cheet and modificaitons of cheet data.
    """
    def __init__(self, name, key, context, description = None, note = None, tags = None):
        self.name = name
        self.key = key
        self.context = context
        self.description = description
        self.note = note
        self.tags = tags

    @classmethod
    def from_json(cls, cheet_as_json: str) -> 'Cheet':
        """Takes a single entry, as json, and creates an entry object."""
        cheet = json.loads(cheet_as_json)
        return cls(
            name = cheet['name'],
            key = cheet['key'],
            context = cheet['context'],
            description = cheet['description'],
            note = cheet['note'],
            tags = cheet['tags']
        )

    def as_dict(self):
        return {
            'name' : self.name,
            'key' : self.key,
            'context' : self.context,
            'description' : self.description,
            'note' : self.note,
            'tags' : self.tags
        }

    def as_json(self):
        return json.dumps(self.as_dict())

    def edit(self, field: str, value):
        """arbitrary field editing.  Adds tags - to remove a tag use rm_tag"""
        if getattr(self, field) is None:
            raise MissingFieldException("attempted to edit a field")
        if field == "tags":
            self.tags.append(value)
        setattr(self, field, value)

    def rm_tag(self, tag: str):
        self.tags.remove(tag)
        

    def __repr__(self):
        tags = ', '.join(self.tags) if self.tags is not None else 'No tags'
        return(
f"""
---
name: {self.name}
key:  {self.key}
desc: {self.description}
note: {self.note}
tags: {tags}
---
"""
        )
        
    
class MissingFieldException(Exception):
    pass
