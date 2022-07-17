from flask import Blueprint, render_template

from db import db
from config import config

editpage = Blueprint('editpage', __name__,
                     template_folder='templates')


@editpage.route('/')
def home():
    if (cheetfilter := config.get('cheetfilter')) is not None:
        cheets = db.get_by(cheetfilter[0], cheetfilter[1])
    else:
        cheets = db.cheets
    page = render_template("editpage.j2", cheets = cheets, config=config)
    return page
