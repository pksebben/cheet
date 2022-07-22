from core.cheet import Cheet

"""handle all persistence operations"""

class NotFoundError(Exception):
    pass

class DB:
    def __init__(self, cheetfile = 'cheets.json'):
        self.cheetfile = cheetfile
        # lost the whole cheet file once.  This is a precaution.
        with open(cheetfile, "r") as f:
            with open(cheetfile + ".backup", "w") as t:
                t.write(f.read())
        self.cheets = Cheet.load_file(cheetfile)

    def load_file(self, path, append=True):
        """load a set of cheets from a json file"""
        self.cheets.append(Cheet.load_file(path))

    def save(self, path=None):
        """save all cheets to file as json"""
        if path is None:
            path = self.cheetfile
        with open(path, "w") as f:
            f.write(Cheet.schema.dumps(self.cheets, many=True))

    def get(self, id):
        """return cheet by id"""
        for cheet in self.cheets:
            if cheet.id == id:
                return cheet
        raise NotFoundError(f"No cheet by id {id} found.")

    def get_by(self, field, val):
        """return a set of cheets matching val in field"""
        cheets = []
        for cheet in self.cheets:
            d = vars(cheet)
            if d[field] is not None:
                if val in d[field]:
                    cheets.append(cheet)
        return cheets

    def delete(self, id):
        """delete cheet by id"""
        for cheet in self.cheets:
            if cheet.id in id:
                print(f"removed {id}")
                self.cheets.remove(cheet)
        self.save()

    def update(self, cheet):
        """update cheet"""
        self.delete(cheet.id)
        self.cheets.append(cheet)
        self.save()

    def create(self, cheet):
        self.cheets.append(cheet)
        self.save()

db = DB()
