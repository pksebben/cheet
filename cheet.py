"""
Usage: 
  cheet.py KEYBIND ACTION CONTEXT [-d DESCRIPTION] [-n NOTE] [TAGS ...]
  cheet.py rm KEYBIND

Arguments:
  KEYBIND     The keybinding to save.
  ACTION      What the binding accomplishes.
  CONTEXT     Where this binding works e.g. vim, emacs, evil-mode, etc.
  TAGS        Extra tags to add to the entry, for organization and notation.

Options:
  -h --help        Show this screen
  -d DESCRIPTION   Describe what this keybind does, if the action is not descriptive.
  -n NOTE          Notes regarding use, if applicable.

 Cheet is a simplified interface for creating cheat sheets
 in a modular fashion.  It is designed to be extensible
 and minimally invasive to your time and attention.
 Cheet.py creates a keybinding and saves it in keybinds.json.
 Other parts of this package use that data to compile
 prettified, sorted, formatted cheat sheets tailored
 to your specific use.

""" 
import json
import docopt

def extract_kb(args):
    name = args['KEYBIND']
    kb = {
        'description': args['-d'],
        'note' : args['-n'],
        'tags' : args['TAGS'],
    }
    context = args['CONTEXT']
    return (context, name, kb)

def add_to_store(store, kb):
    if kb[0] not in store:
        store[kb[0]] = {}
    if kb[1] in store[kb[0]]:
        ow = input("%s exists in context %s. overwrite? (y/n):" % (kb[1], kb[0]))
        while ow not in ("Y","y","N","n"):
            print("bad input. please input Y, y, N or n.")
            ow = input("%s exists in context %s. overwrite? (y/n):" % (kb[1], kb[0]))
        if ow in ("y" , "Y"):
            store[kb[0]][kb[1]] = kb[2]
            print("stored: %s \nin context: %s" % (kb[1], kb[0]))
    else:
        store[kb[0]][kb[1]] = kb[2]
        print("stored: %s \nin context: %s" % (kb[1], kb[0]))

def main():
    args = docopt.docopt(__doc__, version="Cheet 0.1")
    keybind = extract_kb(args)
    keybind_list = json.load(open("keybinds.json", "r"))
    add_to_store(keybind_list, keybind)
    json.dump(keybind_list, open("keybinds.json", "w"))
    return 1


if __name__ == "__main__":
    main()

# TODO: fix docopt to show the whole documentation message when no options are passed.
