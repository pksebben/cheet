from flask import Blueprint, render_template, request, redirect

from core.cheet import Cheet


api = Blueprint('api', __name__,
                template_folder='templates')

@api.route('/update/<id>', methods=["POST"])
def update(id):
    """updates display with selected cheets"""
    print(f"attempting to update {id}")

    f = request.form

    name = f.get('name')
    id = f.get('id')
    key = f.get('key')
    context = f.get('context')
    description = f.get('description')
    note = f.get('note')
    tags = f.get('tags')        # these will have to be mutated
    # clientside, probs

    cheet = Cheet(name,
                  key,
                  context,
                  description if len(description) >= 1 else None,
                  note if len(note) >= 1 else None,
                  [tag for tag in tags.split(" ")] if tags is not None else None,
                  id)
    cheet.pprint()


    return redirect('/editpage')

@api.route('/get', methods=['GET', 'POST'])
def get():
    if request.method == 'POST':
        searchfor = request.form['searchfor']
        searchin = request.form['searchin']
        cm.return_by(searchin, searchfor)
    else:
        return Cheet.schema.dumps(cm.cheets, many=True)
