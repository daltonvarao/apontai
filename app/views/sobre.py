from flask import Blueprint, render_template

sobre_bp = Blueprint('sobre',
                    __name__,
                    url_prefix='/')

@sobre_bp.route('/sobre')
def index_sobre():
    return render_template('sobre/index.html')
