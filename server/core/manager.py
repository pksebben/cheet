import json
import random
import string
import lorem
from core.cheet import Cheet, CheetSchema

class CheetManager:
    """
    Load and modify cheets, select by tag or context.
    """
    def __init__(self):
        self.cheets = []
        self.selected_cheets = []

    # def load_json(self, filename):
        # with open(filename, "r") as f:
            # self.add_cheets(json.load(f))

    # def save_json(self, filename):
        # with open(filename, "w", encoding="utf-8") as f:
            # json.dump(self.cheets, f)

    # def add_cheets(self, cheets):
    #     for i in cheets:
    #         self.add_cheet(i)

    # def add_cheet(self, cheet):
    #     if cheet in self.cheets:
    #         pass
    #     else:
    #         self.cheets.append(cheet)

    # def select_all(self):
    #     self.selected_cheets = self.cheets

    # def select_tag(self, tag):
    #     self.selected_cheets = []
    #     for i in self.cheets:
    #         if tag in i.tags:
    #             self.selected_cheets.append(i)

    # def select_context(self, context):
    #     self.selected_cheets = []
    #     for i in self.cheets:
    #         if i.context == context:
    #             self.selected_cheets.append(i)

    # def return_by(self, field, value):
    #     cheetlist = []
    #     for i in cheets:
    #         cheet = dict(i)
    #         if cheet[field] == value:
    #             cheetlist.append(i)

    #     return cheetlist

    # def load(self, cheets):
    #     print(f"loaded cheets:  {cheets}")
    #     self.cheets = cheets

    # def test_populate(self):
    #     for tag in ['test_one', 'test_two', 'test_three']:
    #         for context in ['vim', 'emacs', 'bash']:
    #             for name in ['bob', 'alice', 'enoch']:
    #                 ipsum = random.choice([lorem.sentence,
    #                                        lorem.paragraph])
    #                 cheet = Cheet(name,
    #                               random.choice(string.ascii_letters),
    #                               context,
    #                               ipsum(),
    #                               "no notes",
    #                               [tag])
    #                 self.cheets.append(cheet)

    # def pprint(self):
    #     print(Cheet.schema.dumps(self.selected_cheets, many=True, indent=2))
