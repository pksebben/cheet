"""
Usage: 
  cheet.py KEYBIND ACTION CONTEXT [-d DESCRIPTION] [-n NOTE] [TAGS ...]
  cheet.py rm KEYBIND
  cheet.py ls
  cheet.py

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

 Creating cheat sheets

 Cheet creates a file 'keybinds.json' that represents a dict of 
 keybind information like context, keystroke, name, and description
 and then processes that file into a jinja template, finally rendering
 using a tool like google-chrome-headless.  It was designed to isolate
 each step of the process such that it should be trivial for anyone 
 with the intent to hack on it and change some or another component
 without affecting the way the rest of it works.  For example, if 
 the provided cli is not to your liking, simply make sure that your
 custom implementation creates a json with the same fieldnames
 and the compilation and rendering steps should work as intended.
 Alternatively, if the output isn't to your taste you could modify 
 the html / css to your preference, or pick another way to display the 
 data, and the design is hopefully such that none of the other bits 
 of the program should get in your way.

 The Cheet cli

 Cheet's default cli offers two options for creating cheets.  You may 
 invoke it straight from the shell, passing in the options defined in 
 this docstring, or you may start it without arguments to access the 
 interactive cli.  From there, the prompts should guide you through 
 creation, deletion, editing, and management of your cheat sheet.
 
 Compilation / Rendering

 Both of the rendering engines have external dependancies as of this
 writing.  There's chrome headless, which requires you to have google 
 chrome installed and accessible via your system's PATH, and there's imgkit,
 which depends on a wkhtmltopdf installation (available via apt on debian
 systems).  NOTE: at the moment, only chrome-headless works.  

 That said, you may choose to compile without rendering.  The default 
 mode of Cheet outputs a file 'cs_final.html' that should be viewable 
 in-browser or by any other method you choose to view webpages.

MODULES
---------------
cheet.py          ::  Manage cheet entries
cheet_compile.py  ::  Compile cheet sheet to output

""" 
import json
import docopt

import cheet_compile


def extract_kb(args):
    kb = {
        'name' : args['ACTION'],
        'key' : args['KEYBIND'],
        'description': args['-d'] if args['-d'] else None,
        'note' : args['-n'] if args['-n'] else "No notes",
        'tags' : args['TAGS'] if args['TAGS'] else None, 
        'context' : args['CONTEXT']
    }
    return kb


def add_to_store(store, kb):
    """this is a crap way to store data.  Makes it hard to use later."""
    for item in store:
        if item['context'] == kb['context'] and item['name'] == kb['name']:
            ow = input("%s exists in context %s. overwrite? (y/n):" % (kb['name'], kb['context']))
            while ow not in ("Y","y","N","n"):
                print("bad input. please input Y, y, N or n.")
                ow = input("%s exists in context %s. overwrite? (y/n):" % (kb['name'], kb['context']))
                if ow in ("y" , "Y"):
                    store.remove(item) # TODO: this is prolly wrong
                    store.append(kb)
                    print("stored: %s \nin context: %s" % (kb[1], kb[0]))
    else:
        store.append(kb)
        print("stored: %s \nin context: %s" % (kb['name'], kb['context']))

      

def prompt_input(options, prompt=None):
    if prompt:
        print(prompt)
    cmd = input("\n" + str(options) + ":")
    if any(opt in cmd for opt in options):
        return cmd
    else:
        print("sorry, I didn't understand that")
        return prompt_input(options, prompt)

def validate(_input):
    pass

def clear_output():
    for i in range(15):
        print('\n')
    
def loop():
    kb_list = json.load(open("keybinds.json", "r"))
    prompt = "\nyou may manage your keybind store here.\n\nls to list keybindings\nrm <INDEX> to remove a keybinding \ncat <INDEX> to print a verbose definition of a keybinding \nvi <INDEX> to edit a keybinding \n"
    options = ['ls', 'rm', 'vi', 'cat', 'q', 'Q', 'h', 'help']
    command = None
    print (prompt)

    while command != "q" or "Q":
        command = None
        command = prompt_input(options)
        if command in "ls":
            list_kb(kb_list)               # TODO: create me
        elif command in "q":
            exit()
        elif command in "vi":
            kb_list.append(add_new_kb())
            save_kb_list(kb_list)
            save_and_compile()
        elif command in ['h','help']:
            print(prompt)
        else:
            try:
                (command, index) = command.split(" ")
                index = int(index)
                if command in "rm":
                    removed = kb_list.pop(index)
                    save_kb_list(kb_list)
                    print("successfully removed %s" % (removed['name']))
                elif command in "vi":
                    new_kb_def = edit_kb(kb_list[index])
                    kb_list[index] = new_kb_def
                    save_kb_list(kb_list)
                elif command in "cat":
                    list_verbose(kb_list[index])
            except ValueError:
                print("I'm sorry, but I didn't understand that.  Did you mean to include an index number?")
            except TypeError:
                print("The second argument must be an index number.")

def add_new_kb():
    print("Adding a keybinding to the cheet sheet.")
    kb = {
        'name': '',
        'key': '',
        'description': '',
        'note': '',
        'tags' : [],
        'context': ''
    }
    return edit_kb(kb)


def edit_kb(kb):
    options = list(kb.keys())
    options.append('q')
    while True: 
        clear_output()
        print("\nedit your keybinding here. Which field would you like to edit? Enter q to save changes and exit.")
        list_verbose(kb)
        cmd = prompt_input(options)
        if cmd in 'q':
            return kb
        if isinstance(kb[cmd], str):
            kb[cmd] = input("Enter a new value for %s : " % cmd)
        elif isinstance(kb[cmd], list):
            q = False
            while not q:
                print("\nhere are all the %s in %s" % (cmd, kb['name']))
                for i in kb[cmd]: print(i)
                entry = input("\nEnter a value to put in %s, or q to save changes : " % cmd)
                if entry in 'q':
                    q = True
                else:
                    kb[cmd].append(entry)

    
def save_kb_list(kb_list):
    json.dump(kb_list, open("keybinds.json", "w"))
    save_and_compile()
        
def list_verbose(kb):
    print("\n")
    for k in kb.keys(): 
        print("%s  ::  %s" % (k, kb[k]))
        
def list_kb(store):

    count = 0
    print("INDEX  |  ACTION  |  KEYBIND  |  DESCRIPTION")

    for kb in store:
        print("%s :: %s - %s " % (count, kb['name'], kb['key']))
        count = count+1

def save_and_compile():
    cheet_compile.compile_cheetsheet()
    cheet_compile.save_cheetsheet(cheet_compile.compile_cheetsheet())
    cheet_compile.chrome_headless_render()

def parse_input():
    pass

def main():
    # TODO: split up into functions // flesh out more of the cli
    # TODO: See if you can boil this down to a single input cmd in the loop.
    args = docopt.docopt(__doc__, version="Cheet 0.1")
    
    keybind = extract_kb(args)
    try:
        keybind_list = json.load(open("keybinds.json", "r"))
    except FileNotFoundError:
        print("No keybinds.json found.  Initializing fresh keybinds.json")
        keybind_list = [] 
    if args['KEYBIND']:
        add_to_store(keybind_list, keybind)
    else:
        loop()

    json.dump(keybind_list, open("keybinds.json", "w"))
    cheet_compile.compile_cheetsheet()
    cheet_compile.save_cheetsheet(cheet_compile.compile_cheetsheet())
    cheet_compile.chrome_headless_render()
    return 1

if __name__ == "__main__":
    main()

# TODO: fix docopt to show the whole documentation message when no options are passed.
