"""Cheet Compile

Cheet Compile will take a list of keybinds and compile it down to html, optionally rendering it to jpeg so it can be used where images are used.

Usage:
  python3 cheet_compile.py [-i INPUT] [-o OUTPUT] [-t TEMPLATE] [-r RENDERER]

Arguments:

Options:
  -i --input INPUT         The json list of keybinds to compile [default: "keybinds.json"]
  -o --output OUTPUT       The name of the file to compile to [default: "cs_final.html"]
  -t --template TEMPLATE   The jinja template to load [default: "cs_template.html"]
  -r --renderer RENDERER   The renderer to use. Details below [default: "chrome_headless"]

# INPUT
Cheet Compile takes a list of keybinds in json.  INPUT is a string representing a path to this file. To generate the list of keybinds, you have options.  You can use the included cheet.py to generate a keybinds.json, or roll your own solution.  If rolling your own, make sure to create a json file that follows this format:
[
{
  "KEYBIND": <str>,
  "ACTION": <str>,
  "CONTEXT": <str>,
  "TAGS" : [ <str>, ...],
  "NOTE" : <str> or <null>,
  "DESC" : <str> or <null>
},
...
]

# RENDERER
Cheet compile can use a number of methods for creating a final render of your cheet sheet.

## Chrome Headless
Requires google-chrome to be on your machine and available in your PATH.  Also requires bash, as google-chrome is invoked using a subprocess.Popen interface

NOTES:
This is currently broken for anyone other than myself.  
Also, the docs are aspirational.  Not all the flags work as intended, yet.
"""
import os
from jinja2 import Template
import json
import imgkit
import docopt
from subprocess import Popen, PIPE
import shlex
import subprocess

PROJECT_DIR = "/home/coffee/code/cheet"

def compile_cheetsheet(cheetsheet = "keybinds.json", template = "rendering/cs_template.html"):
    template_html = open(template, "r").read()
    t = Template(template_html)
    return t.render(cheats=json.load(open(cheetsheet, "r")))

def save_cheetsheet(sheet):
    f = open("rendering/cs_final.html", "w")
    f.write(sheet)
    print("saved sheet to cs_final.html")

def render_cheetsheet(sheet = "rendering/cs_final.html"):
    imgkit.from_file(sheet, "/cheet.jpg")

def chrome_headless_render():
    # TODO: check if google-chrome is on the system, if not throw
    path = "" + PROJECT_DIR + "/rendering/cs_final.html"
    cmd = r"google-chrome --headless --disable-gpu --disable-application-cache --screenshot --window-size=1920,1080 --hide-scrollbars file://" + PROJECT_DIR + "/rendering/cs_final.html"
    proc = Popen([cmd], cwd=PROJECT_DIR, stdout=PIPE, stderr=PIPE, shell=True)
    stdout, stderr = proc.communicate()
    print("should have rendered")

def set_desktop(f = "file://" + PROJECT_DIR + "/screenshot.png"):
    # This requires that certain environment variables are set.
    set_envir()
    cmd = "gsettings set org.gnome.desktop.background picture-uri %s" % f
    process = Popen(["/bin/sh", "-c", cmd], stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()

def set_envir():
    pid = subprocess.check_output(["pgrep", "gnome-session"]).decode("utf-8").strip().split("\n")[0]
    cmd = "grep -z DBUS_SESSION_BUS_ADDRESS /proc/"+pid+"/environ|cut -d= -f2-"
    os.environ["DBUS_SESSION_BUS_ADDRESS"] = subprocess.check_output(
        ['/bin/bash', '-c', cmd]).decode("utf-8").strip().replace("\0", "")

    
if __name__ == "__main__":
    save_cheetsheet(compile_cheetsheet())
    chrome_headless_render()
    # set_desktop()

# TODO: imgkit's rendering isn't the best.  What other options are out there?
# better alternatives may be found here: https://stackoverflow.com/questions/10721884/render-html-to-an-image
# more in depth description of using headless chrome for rendering: https://developers.google.com/web/updates/2017/04/headless-chrome#cli
