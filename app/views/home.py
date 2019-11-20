from flask import Blueprint, render_template, request_tearing_down


home_bp = Blueprint('home',
                    __name__,
                    template_folder='templates')


@home_bp.route('/')
def home_index():
    return render_template('home/index.html')
