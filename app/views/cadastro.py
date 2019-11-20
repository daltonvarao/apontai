from flask import Blueprint, render_template, session, request, flash
from app.models.usuario import Usuario, db

cadastro_bp = Blueprint('cadastro',
                    __name__,
                    url_prefix='/cadastro')


@cadastro_bp.route('/', methods=["GET", "POST"])
def new_cadastro():
    if request.method == "POST":
        
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        confirma_senha = request.form.get('confirma_senha')

        user_exists = db.session.query(Usuario).filter_by(email=email).first() 
        
        if user_exists:
            flash('Email já cadastrado, tente outro!', 'danger')

        if senha != confirma_senha:
            flash('Senhas não conferem, tente novamente!', 'danger')


        return render_template('cadastro/index.html', show_navigation=True)
    return render_template('cadastro/index.html', show_navigation=True)
