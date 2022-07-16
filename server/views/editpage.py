from flask import Blueprint, render_template
# from flask_wtf import FlaskForm, csrf
from wtforms import StringField, TextAreaField, Form
from wtforms.validators import DataRequired

from db import db
from config import config

editpage = Blueprint('editpage', __name__,
                     template_folder='templates')

@editpage.route('/editpage')
def home():
    if (cheetfilter := config.get('cheetfilter')) is not None:
        cheets = db.get_by(cheetfilter[0], cheetfilter[1])
    else:
        cheets = db.cheets
    page = render_template("editpage.j2", cheets = cheets, config=config)
    return page
