from flask import Blueprint, render_template, request, redirect

from core.cheet import Cheet
from db import db


api = Blueprint('api', __name__,
                template_folder='templates')

@api.route('/update/<id>', methods=["POST"])
def update(id):
    """updates display with selected cheets"""
    f = request.form
    cheet = Cheet(f.get('name'),
                  f.get('key'),
                  f.get('context'),
                  f.get('description'),
                  f.get('note'),
                  f.get('tags'),
                  f.get('id'))

    db.update(cheet)

    return redirect('/editpage')

@api.route('/get', methods=['GET', 'POST'])
def get():
    if request.method == 'POST':
        searchfor = request.form['searchfor']
        searchin = request.form['searchin']
        db.get_by(searchin, searchfor)
    else:
        return Cheet.schema.dumps(cm.cheets, many=True)

@api.route('/create', methods=["POST"])
def create():
    f = request.form
    cheet = Cheet(f.get('name'),
                  f.get('key'),
                  f.get('context'),
                  f.get('description'),
                  f.get('note'),
                  f.get('tags'))
    db.create(cheet)
    return redirect('/editpage')

@api.route('/delete/<id>', methods=['GET'])
def delete(id):
    db.delete(id)
    return redirect('/editpage')
