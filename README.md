# Cheet

Make personalized, customized cheat sheets that have only what you want in them.  Compile lists of commands into prettified, well formatted documents to put in documentation, print, or on your desktop background for quick reference.

I got sick of having cheat sheets made by other people.  Not because they were bad in general, but because invariably they had at most five or six things I wanted on them, and about a hundred things I didn't want on them (either because I didn't need them or I had the muscle memory already.)

# Requirements

Cheet_compile uses headless chrome to render sheets, which should be available if you have chrome installed.

After pulling the repo and creating a venv, you must `pip install -r requirements.txt`

# Usage / Workflow

Each piece of cheet is decoupled such that you should be able to implement custom modules at any stage.  That said, the current workflow looks like this:

## 1. Create cheets with the cli

```bash
python3 cheet.py <keybinding> <action> <context> [-d <description>] [-n <note>] [<tags> ...]
```

This outputs to a simple json file ```cheet-keybinds.json``` that stores all your cheets for you.

## 2. Compile to output

```bash
python3 cheet_compile.py
```

This (currently) compiles your list of cheets into html using jinja templating, and renders them using google-chrome in headless mode.

# Roadmap

- Allow compiling into other formats / rendering to jpeg / tiff / png / pdf
- Creation of subsets of saved cheets, management of cheets and organization by tag / context / whatever
- Emacs integration to save, search, and show keybindings
