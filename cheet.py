"""Cheet

 Cheet is a simplified interface for creating cheat sheets
 in a modular fashion.  It is designed to be extensible
 and minimally invasive to your time and attention.
 Cheet.py creates a keybinding and saves it in keybinds.json.
 Other parts of this package use that data to compile
 prettified, sorted, formatted cheat sheets tailored
 to your specific use.


Usage: 
  python3 cheet.py KEYBIND ACTION CONTEXT [options] [TAGS ...]

Arguments:
  KEYBIND     The keybinding to save.
  ACTION      What the binding accomplishes.
  CONTEXT     Where this binding works e.g. vim, emacs, evil-mode, etc.
  TAGS        Extra tags to add to the entry, for organization and notation.

Options:
  -h --help        Show this screen
  -d DESCRIPTION   Describe what this keybind does, if the action is not descriptive.
  -n NOTE          Notes regarding use, if applicable.
  -D               Do not compile.  Use this if compiling using non-default settings.


""" 
import json
import docopt

def trim_args(args):
    del args["--help"]
    del args["-D"]
    args["NOTE"] = args.pop("-n")
    args["DESC"] = args.pop("-d")
    return args

def main():
    args = docopt.docopt(__doc__, version="Cheet 0.1")
    keybind = trim_args(args)
    keybind_list = json.load(open("keybinds.json", "r"))
    keybind_list.append(keybind)
    json.dump(keybind_list, open("keybinds.json", "w"))
    return 1


if __name__ == "__main__":
    main()

# TODO: fix docopt to show the whole documentation message when no options are passed.
