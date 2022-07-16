from core.cheet import Cheet
from core.manager import CheetManager

"""handle all persistence operations"""

class NotFoundError(Exception):
    pass

class DB:
    def __init__(self, cheetfile = 'cheets.json'):
        self.cheetfile = cheetfile
        # lost the whole cheet file once.  This is a precaution.
        with open(cheetfile, "r") as f:
            with open(cheetfile + ".backup", "w") as t:
                f.write(t)
        self.cheets = Cheet.load_file(cheetfile)


    def load_file(self, path):
        self.cheets = Cheet.load_file(path)

    def save(self, path=self.cheetfile):
        with open(path, "w") as f:
            f.write(Cheet.schema.dumps(self.cheets, many=True))

    def get(self, id):
        for cheet in self.cheets:
            if cheet.id == id:
                return cheet
        raise NotFoundError(f"No cheet by id {id} found.")

    def get_by(self, field, val):
        cheets = []
        for cheet in self.cheets:
            d = dict(cheet)
            if val in d[field]:
                cheets.append(cheet)
        if cheets == []:
            raise NotFoundError(f"we found no cheets with a {field} = {val}")
        return cheets

    def delete(self, id):
        print(f"deleting id: {id}")
        for cheet in self.cheets:
            if cheet.id in id:
                print(f"removed {id}")
                self.cheets.remove(cheet)
        self.save()

    def update(self, cheet):
        self.delete(cheet.id)
        self.cheets.append(cheet)
        self.save()

    def create(self, cheet):
        self.cheets.append(cheet)
        self.save()

db = DB()
