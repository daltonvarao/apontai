from flask import Blueprint, render_template
from app.models.models import Usuario

login_bp = Blueprint('login',
                    __name__,
                    url_prefix='/')

@login_bp.route('/login')
def index_login():
    return render_template('login/index.html', show_navigation=True)
