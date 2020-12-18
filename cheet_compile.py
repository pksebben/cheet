from jinja2 import Template
import json


def compile_cheetsheet(cheetsheet = "keybinds.json", template = "cheet_sheet.html"):
    template_html = open(template, "r").read()
    t = Template(template_html)
    return t.render(cheats=json.load(open(cheetsheet, "r")))

def save_cheetsheet(sheet):
    f = open("cheet_sheet_final.html", "w")
    f.write(sheet)
    
if __name__ == "__main__":
    save_cheetsheet(compile_cheetsheet())
