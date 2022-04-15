# Cheet

Make personalized, customized cheat sheets that have only what you want in them.  Compile lists of commands into prettified, well formatted documents to put in documentation, print, or on your desktop background for quick reference.

I got sick of having cheat sheets made by other people.  Not because they were bad in general, but because invariably they had at most five or six things I wanted on them, and about a hundred things I didn't want on them (either because I didn't need them or I had the muscle memory already.)

# Requirements

cheet_compile uses imgkit, which requires you to have wkhtmltopdf installed.  If you're using your own rendering solution you won't need it.

```sh
sudo apt install wkhtmltopdf
```

# Usage / Workflow

Each piece of cheet is decoupled such that you should be able to implement custom modules at any stage.  That said, the current workflow looks like this:

## 1. Create cheets with the cli

The easiest method is to simply run `python3 cheet.py`, which will open the interactive editor.

You can also create cheets as a one-liner:

```bash
python3 cheet.py <keybinding> <action> <context> [-d <description>] [-n <note>] [<tags> ...]
```

This outputs to a simple json file ```keybinds.json``` that stores all your cheets for you.

After either method, changes made to cheets will attempt to autocompile using `cheet_compile.py` (currently, this implements chrome-headless to render to a .png, which you can set your desktop to.)

## 2. Compile to output

Cheets should autocompile after each save.  However, if you want to compile your cheet list without editing it in the `cheet` editor, you can

```bash
python3 cheet_compile.py
```

This (currently) compiles your list of cheets into html using jinja templating, and renders them using google-chrome in headless mode.

# Roadmap

- Implement configuration for save dir / etc.
- Allow compiling into other formats / rendering to jpeg / tiff / png / pdf
- Creation of subsets of saved cheets, management of cheets and organization by tag / context / whatever
- Emacs integration to save, search, and show keybindings
