import html

from flask import Blueprint, render_template, request, redirect

from core.cheet import Cheet
from db import db
from config import config


api = Blueprint('api', __name__,
                template_folder='templates')

def extract_cheet(form):
    """escape html from form fields and return cheet"""
    d = {}
    for key in form.keys():
        d[key] = html.unescape(form.get(key))
    cheet = Cheet.from_dict(d)
    return cheet

@api.route('/configure/cheetfilter', methods=['POST'])
def configure_cheetfilter():
    field = request.form.get('field')
    val = request.form.get('value')
    config['cheetfilter'] = (field, val)
    if request.form.get('clear') is not None:
        del config['cheetfilter']
    return redirect('/')

@api.route('/update', methods=["POST"])
def update():
    """updates display with selected cheets"""
    cheet = extract_cheet(request.form)
    db.update(cheet)

    return redirect('/')

@api.route('/get', methods=['GET', 'POST'])
def get():
    """return json string of cheets"""
    if request.method == 'POST':
        searchfor = request.form['searchfor']
        searchin = request.form['searchin']
        db.get_by(searchin, searchfor)
    else:
        return Cheet.schema.dumps(cm.cheets, many=True)

@api.route('/create', methods=["POST"])
def create():
    """create a cheet from formdata"""
    cheet = extract_cheet(request.form)
    db.create(cheet)
    return redirect('/')

@api.route('/delete/<id>', methods=['GET'])
def delete(id):
    """delete cheet by id"""
    db.delete(id)
    return redirect('/')

@api.route('/addtag/<id>')
def addtag(id):
    cheet = db.get(id)
    cheet.tags.append('newtag')
    return redirect('/')

@api.route('/remtag/<id>/<tag>')
def remtag(id, tag):
    cheet = db.get(id)
    cheet.tags = cheet.tags.remove(tag)
    db.update(cheet)
    return redirect('/')

@api.route('/vimedit/<id>', methods=['GET'])
def vimedit(id):
    """open vim in the server process to edit a cheet by id"""
    if id in 'newcheet':
        cheet = Cheet('required','required','required','required')
    else:
        cheet = db.get(id)
    cheet = cheet.vim_edit()
    db.update(cheet)
    return redirect('/')
