import json
import tempfile
import subprocess
from uuid import uuid4
from marshmallow import Schema, fields, post_load
from marshmallow.exceptions import ValidationError

# import cheet_compile
import random

class CheetSchema(Schema):
    name = fields.Str()
    id = fields.Str(default=str(uuid4()))
    key = fields.Str()
    context = fields.Str()
    description = fields.Str()
    note = fields.Str(allow_none=True)
    tags = fields.List(fields.Str(), allow_none=True)

    @post_load
    def make_cheet(self, data, **kwargs):
        return Cheet(**data)


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
            cheet = Cheet('error',
                          'N/A',
                          'err',
                          f'There was a validation error loading {path}')
            print(f"Validation error for {path}: {e}")
            return [cheet]

    @classmethod
    def from_dict(self, cdict):
        required = ['name', 'key', 'context', 'description']
        for k in required:
            if k not in cdict.keys():
                raise ValidationError(f"missing key: {k}")

        cheet = Cheet(
            cdict.get('name'),
            cdict.get('key'),
            cdict.get('context'),
            cdict.get('description'),
            cdict.get('note'),
            cdict.get('tags'),
            cdict.get('id')
        )
        return cheet

    def __init__(self,
                 name,
                 key,
                 context,
                 description,
                 note = None,
                 tags = None,
                 id = None):
        self.name = name
        self.key = key
        self.context = context
        self.description = description
        self.note = note
        self.tags = tags
        if id is not None:
            self.id = id
        else:
            self.id = str(uuid4())


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

# def prompt_input(options, prompt=None):
#     if prompt:
#         print(prompt)
#     cmd = input("\n" + str(options) + ":")
#     if any(opt in cmd for opt in options):
#         return cmd
#     else:
#         print("sorry, I didn't understand that")
#         return prompt_input(options, prompt)

# def loop(kb_list):
#     prompt = "\nyou may manage your keybind store here.\n\nls to list keybindings\nrm <INDEX> to remove a keybinding \ncat <INDEX> to print a verbose definition of a keybinding \nvi <INDEX> to edit a keybinding \n"
#     options = ['ls', 'rm', 'vi', 'cat', 'q', 'Q', 'h', 'help', 'test']
#     command = None
#     print (prompt)

#     while command != "q" or "Q":
#         command = None
#         command = prompt_input(options)
#         if command in "ls":
#             list_kb(kb_list)               # TODO: create me
#         elif command in "q":
#             exit()
#         elif command in "vi":
#             kb_list.append(add_new_kb())
#             save_kb_list(kb_list)
#             save_and_compile()
#         elif command in ['h','help']:
#             print(prompt)
#         elif command in "test":
#             test_kb = {
#                 'name': 'test-kb-' + str(random.randrange(1000)) ,
#                 'key': 't',
#                 'description': '',
#                 'note': '',
#                 'tags' : [],
#                 'context': 'testing'
#             }
#             kb_list.append(test_kb)
#             save_kb_list(kb_list)
#         else:
#             try:
#                 (command, index) = command.split(" ")
#                 index = int(index)
#                 if command in "rm":
#                     removed = kb_list.pop(index)
#                     save_kb_list(kb_list)
#                     print("successfully removed %s" % (removed['name']))
#                 elif command in "vi":
#                     new_kb_def = edit_kb(kb_list[index])
#                     kb_list[index] = new_kb_def
#                     save_kb_list(kb_list)
#                 elif command in "cat":
#                     list_verbose(kb_list[index])
#             except ValueError:
#                 print("I'm sorry, but I didn't understand that.  Did you mean to include an index number?")
#             except TypeError:
#                 print("The second argument must be an index number.")

# def add_new_kb():
#     print("Adding a keybinding to the cheet sheet.")
#     kb = {
#         'name': '',
#         'key': '',
#         'description': '',
#         'note': '',
#         'tags' : [],
#         'context': ''
#     }
#     return edit_kb(kb)


# def edit_kb(kb):
#     options = list(kb.keys())
#     options.append('q')
#     while True:
#         clear_output()
#         print("\nedit your keybinding here. Which field would you like to edit? Enter q to save changes and exit.")
#         list_verbose(kb)
#         cmd = prompt_input(options)
#         if cmd in 'q':
#             return kb
#         if isinstance(kb[cmd], str):
#             kb[cmd] = input("Enter a new value for %s : " % cmd)
#         elif isinstance(kb[cmd], list):
#             q = False
#             while not q:
#                 print("\nhere are all the %s in %s" % (cmd, kb['name']))
#                 for i in kb[cmd]: print(i)
#                 entry = input("\nEnter a value to put in %s, or q to save changes : " % cmd)
#                 if entry in 'q':
#                     q = True
#                 else:
#                     kb[cmd].append(entry)


# def save_kb_list(kb_list):
#     json.dump(kb_list, open("keybinds.json", "w"))
#     save_and_compile()

# def list_verbose(kb):
#     print("\n")
#     for k in kb.keys():
#         print("%s  ::  %s" % (k, kb[k]))

# def list_kb(store):

#     count = 0
#     print("INDEX  |  ACTION  |  KEYBIND  |  DESCRIPTION")

#     for kb in store:
#         print("%s :: %s - %s " % (count, kb['name'], kb['key']))
#         count = count+1

# def save_and_compile():
#     cheet_compile.compile_cheetsheet()
#     cheet_compile.save_cheetsheet(cheet_compile.compile_cheetsheet())
#     cheet_compile.chrome_headless_render()
#     cheet_compile.set_desktop()

# def parse_input():
#     pass

# def kb_list():
#     try:
#         keybind_list = json.load(open("keybinds.json", "r"))
#     except FileNotFoundError:
#         print("No keybinds.json found.  Initializing fresh keybinds.json")
#         keybind_list = []
#     return keybind_list



# def main():
#     # TODO: split up into functions // flesh out more of the cli
#     # TODO: See if you can boil this down to a single input cmd in the loop.

#     keybind_list = kb_list()
#     loop(keybind_list)

#     json.dump(keybind_list, open("keybinds.json", "w"))
#     cheet_compile.compile_cheetsheet()
#     cheet_compile.save_cheetsheet(cheet_compile.compile_cheetsheet())
#     cheet_compile.chrome_headless_render()
#     return 1

# if __name__ == "__main__":
#     main()

# # TODO: fix docopt to show the whole documentation message when no options are passed.
