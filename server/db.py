from core.cheet import Cheet
from core.manager import CheetManager

"""handle all persistence operations"""

class NotFoundError(Exception):
    pass

class DB:
    def __init__(self, cheetfile = 'cheets.json'):
        self.cheetfile = cheetfile
        self.cheets = Cheet.load_file(cheetfile)

    def load_file(self, path):
        self.cheets = Cheet.load_file(path)

    def save(self):
        with open(self.cheetfile, "w") as f:
            f.write(Cheet.schema.dumps(self.cheets))

    def get(self, id):
        for cheet in self.cheets:
            if cheet.id == id:
                return cheet
        raise NotFoundError(f"No cheet by id {id} found.")

    def get_by(self, field, val):
        cheets = []
        for cheet in self.cheets:
            d = dict(cheet)
            if d[field] == val:
                cheets.append(cheet)
        if cheets == []:
            raise NotFoundError(f"we found no cheets with a {field} = {val}")
        return cheets

    def delete(self, id):
        cheet = None
        for cheet in self.cheets:
            if cheet.id == id:
                self.cheets.remove(cheet)

    def update(self, cheet):
        self.cheets.remove(id)
        self.cheets.append(cheet)

db = DB()