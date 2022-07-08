import json
import random
import string
from core.cheet import Cheet, CheetSchema

class CheetManager:
    """
    Load and modify cheets, select by tag or context.
    """
    def __init__(self):
        self.cheets = []
        self.selected_cheets = []

    def load_json(self, filename):
        with open(filename, "r") as f:
            self.add_cheets(json.load(f))

    def save_json(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.cheets, f)

    def add_cheets(self, cheets):
        for i in cheets:
            self.add_cheet(i)

    def add_cheet(self, cheet):
        if cheet in self.cheets:
            pass
        else:
            self.cheets.append(cheet)

    def select_all(self):
        self.selected_cheets = self.cheets

    def select_tag(self, tag):
        self.selected_cheets = []
        for i in self.cheets:
            if tag in i.tags:
                self.selected_cheets.append(i)

    def select_context(self, context):
        self.selected_cheets = []
        for i in self.cheets:
            if i.context == context:
                self.selected_cheets.append(i)

    def test_populate(self):
        for tag in ['test_one', 'test_two', 'test_three']:
            for context in ['vim', 'emacs', 'bash']:
                for name in ['bob', 'alice', 'enoch']:
                    cheet = Cheet(name,
                                  random.choice(string.ascii_letters),
                                  context,
                                  "test description",
                                  "no notes",
                                  [tag])
                    self.cheets.append(cheet)

    def pprint(self):
        print(Cheet.schema.dumps(self.selected_cheets, many=True, indent=2))
