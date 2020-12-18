"""
cheet_compile
This will take a list of keybinds and compile it down to html, optionally rendering it to jpeg so it can be used where images are used.
"""
from jinja2 import Template
import json
import imgkit


def compile_cheetsheet(cheetsheet = "keybinds.json", template = "cs_template.html"):
    template_html = open(template, "r").read()
    t = Template(template_html)
    return t.render(cheats=json.load(open(cheetsheet, "r")))

def save_cheetsheet(sheet):
    f = open("cs_final.html", "w")
    f.write(sheet)

def render_cheetsheet(sheet = "cs_final.html"):
    imgkit.from_file(sheet, "/cheet.jpg")
    
if __name__ == "__main__":
    save_cheetsheet(compile_cheetsheet())
    render_cheetsheet()

# TODO: imgkit's rendering isn't the best.  What other options are out there?
