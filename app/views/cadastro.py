from flask import Blueprint, render_template, session

cadastro_bp = Blueprint('cadastro',
                    __name__,
                    url_prefix='/cadastro')

@cadastro_bp.route('/')
def index_cadastro():
    return render_template('cadastro/index.html', show_navigation=True)