"""
This is the old cli for cheet.  I wanted to keep it around so I could
port it over when I reimplement that functionality, but it shouldn't
live in a file that is currently in such heav use
"""


def prompt_input(options, prompt=None):
    if prompt:
        print(prompt)
    cmd = input("\n" + str(options) + ":")
    if any(opt in cmd for opt in options):
        return cmd
    else:
        print("sorry, I didn't understand that")
        return prompt_input(options, prompt)

def loop(kb_list):
    prompt = "\nyou may manage your keybind store here.\n\nls to list keybindings\nrm <INDEX> to remove a keybinding \ncat <INDEX> to print a verbose definition of a keybinding \nvi <INDEX> to edit a keybinding \n"
    options = ['ls', 'rm', 'vi', 'cat', 'q', 'Q', 'h', 'help', 'test']
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
        elif command in "test":
            test_kb = {
                'name': 'test-kb-' + str(random.randrange(1000)) ,
                'key': 't',
                'description': '',
                'note': '',
                'tags' : [],
                'context': 'testing'
            }
            kb_list.append(test_kb)
            save_kb_list(kb_list)
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
    cheet_compile.set_desktop()

def parse_input():
    pass

def kb_list():
    try:
        keybind_list = json.load(open("keybinds.json", "r"))
    except FileNotFoundError:
        print("No keybinds.json found.  Initializing fresh keybinds.json")
        keybind_list = []
    return keybind_list



def main():
    # TODO: split up into functions // flesh out more of the cli
    # TODO: See if you can boil this down to a single input cmd in the loop.

    keybind_list = kb_list()
    loop(keybind_list)

    json.dump(keybind_list, open("keybinds.json", "w"))
    cheet_compile.compile_cheetsheet()
    cheet_compile.save_cheetsheet(cheet_compile.compile_cheetsheet())
    cheet_compile.chrome_headless_render()
    return 1

if __name__ == "__main__":
    main()

# TODO: fix docopt to show the whole documentation message when no options are passed.
