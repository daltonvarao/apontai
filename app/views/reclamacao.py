from flask import Blueprint, render_template, session

reclamacao_bp = Blueprint('reclamacao',
                    __name__,
                    url_prefix='/reclamacao')

@reclamacao_bp.route('/')
def new_reclamacao():
    return render_template('reclamacao/new.html')