from flask import Blueprint, render_template, session, request, redirect, url_for, flash
from app.utils.login import login_required
from app.models.models import Reclamacao, Usuario, db


reclamacao_bp = Blueprint('reclamacao',
                    __name__,
                    url_prefix='/reclamacoes')

@reclamacao_bp.route('/new', methods=['GET', 'POST'])
@login_required
def new_reclamacoes():
    if request.method == 'POST':
        
        tipo = request.form.get('tipo')
        titulo = request.form.get('titulo')
        local = request.form.get('local')
        tempo = request.form.get('tempo')
        descricao = request.form.get('descricao')

        reclamacao = Reclamacao(
                        titulo=titulo,
                        tipo=tipo, 
                        local=local,
                        tempo=tempo,
                        descricao=descricao,
                        usuario_id=session.get('user_id')
                    )
        
        current_user = db.session.query(Usuario).get(int(session.get('user_id')))
        reclamacao.reclamadores.append(current_user)

        db.session.add(reclamacao)
        db.session.commit()

        flash('Reclamação salva', 'success')
        return redirect(url_for('index.index'))

    return render_template('reclamacao/new.html')


@reclamacao_bp.route('/')
def index_reclamacoes():
    status = True if request.args.get('status') == 'solucionados' else False
    
    reclamacoes = db.session.query(Reclamacao).filter_by(fechado=status).all()

    return render_template('reclamacao/index.html', reclamacoes=reclamacoes)


@reclamacao_bp.route('/reclamar/<int:reclamacao_id>')
@login_required
def reclamar(reclamacao_id):
    reclamacao = db.session.query(Reclamacao).get(int(reclamacao_id))
    current_user = db.session.query(Usuario).get(int(session.get('user_id')))
    reclamacao.reclamadores.append(current_user)

    db.session.add(reclamacao)
    db.session.commit()
    flash('Sucesso!', 'success')
    return redirect(url_for('reclamacao.index_reclamacoes', status=['abertos']))


