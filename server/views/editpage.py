from flask import Blueprint, render_template
# from flask_wtf import FlaskForm, csrf
from wtforms import StringField, TextAreaField, Form
from wtforms.validators import DataRequired

from db import db

editpage = Blueprint('editpage', __name__,
                     template_folder='templates')

@editpage.route('/editpage')
def home():
    form = CheetForm()
    page = render_template("editpage.j2", cheets = db.cheets, form=form)
    return page
