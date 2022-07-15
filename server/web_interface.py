from flask import Blueprint, render_template
from wtforms import StringField
from flask_wtf import FlaskForm

from db import db

interface = Blueprint('interface', __name__,
                template_folder='templates')

@interface.route('/edit/<cheetid>')
def edit_cheet(cheetid):

    cheet = db.get(id)
    return render_template('edit_cheet.j2', cheet=cheet)
