from flask import Blueprint, render_template, session

index_bp = Blueprint('index',
                    __name__,
                    url_prefix='/')

@index_bp.route('/')
def index():
    return render_template('index/index.html')
