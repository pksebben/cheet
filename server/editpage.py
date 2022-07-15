from flask import Blueprint, render_template
# from flask_wtf import FlaskForm, csrf
from wtforms import StringField, TextAreaField, Form
from wtforms.validators import DataRequired

from db import db

class CheetForm(Form):
    name = StringField('name')
    id = StringField('id')
    key = StringField('key')
    context = StringField('context')
    description = TextAreaField('description')
    note = StringField('note')
    tags = StringField('tags')

editpage = Blueprint('editpage', __name__,
                     template_folder='templates')


@editpage.route('/editpage')
def home():
    form = CheetForm()
    page = render_template("editpage.j2", cheets = db.cheets, form=form)
    return page
