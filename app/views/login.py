from flask import Blueprint, render_template, session, request, flash, redirect, url_for
from app.models.models import Usuario, db, Reclamacao

login_bp = Blueprint('login',
                    __name__,
                    url_prefix='/')

@login_bp.route('/login', methods=['GET', 'POST'])
def index_login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        usuario = db.session.query(Usuario).filter_by(email=email).first()
        if usuario:
            if usuario.senha != senha:
                flash('Senha incorreta!', 'danger')
            else:
                session['logged_in'] = True
                session['user_id'] = usuario.id
                session['user_name'] = usuario.first_name()
                
                flash(f"Bem vindo {session['user_name']}")
                return redirect(url_for('index.index'))
        else:
            flash('Email não encontrado, tente outro!', 'danger')
        return render_template('login/index.html', show_navigation=True, usuario=usuario)
    return render_template('login/index.html', show_navigation=True)


@login_bp.route('/logout')
def index_logout():
    session.clear()
    flash('Até mais, estamos preparando tudo para quando você voltar!', 'success')
    return redirect(url_for('login.index_login'))
