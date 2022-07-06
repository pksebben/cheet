import json

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

    def add_cheets(self, cheets):
        for i in cheets:
            self.add_cheet(i)

    def add_cheet(self, cheet):
        if cheet in self.cheets:
            pass
        else:
            self.cheets.append(cheet)

    def select_tag(self, tag):
        self.selected_cheets = []
        for i in self.cheets:
            if tag in i['tags']:
                self.selected_cheets.append(i)

    def select_context(self, context):
        self.selected_cheets = []
        for i in self.cheets:
            if i['context'] == context:
                self.selected_cheets.append(i)
