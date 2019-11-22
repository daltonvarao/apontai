from flask import Blueprint, render_template, session, request, redirect, url_for, flash
from app.utils.login import login_required
from app.models.models import Reclamacao, Usuario, db
from werkzeug.utils import secure_filename
import datetime
import os


reclamacao_bp = Blueprint('reclamacao',
                    __name__,
                    url_prefix='/reclamacoes')


UPLOAD_FOLDER = os.path.join(os.getcwd(), 'app/static/img/uploads/')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@reclamacao_bp.route('/new', methods=['GET', 'POST'])
@login_required
def new_reclamacoes():
    if request.method == 'POST':
        
        tipo = request.form.get('tipo')
        titulo = request.form.get('titulo')
        local = request.form.get('local')
        descricao = request.form.get('descricao')

        reclamacao = Reclamacao(
                        titulo=titulo,
                        tipo=tipo, 
                        local=local,
                        descricao=descricao,
                        usuario_id=session.get('user_id')
                    )
        
        current_user = db.session.query(Usuario).get(session.get('user_id'))
        reclamacao.reclamadores.append(current_user)

        db.session.add(reclamacao)
        db.session.flush()

        full_path = ''

        if 'foto' in request.files:
            file = request.files['foto']
        
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(UPLOAD_FOLDER,f'rec{reclamacao.id}-' + filename))

        reclamacao.img_url = f'rec{reclamacao.id}-' + filename
        db.session.commit()

        flash('Reclamação salva', 'success')
        return redirect(url_for('index.index'))

    return render_template('reclamacao/new.html')


@reclamacao_bp.route('/')
def index_reclamacoes():
    status = True if request.args.get('status') == 'solucionados' else False  
    reclamacoes = db.session.query(Reclamacao).filter_by(fechado=status)
    tipo = request.args.get('tipo')

    if tipo:
        reclamacoes = reclamacoes.filter_by(tipo=tipo)

    return render_template('reclamacao/index.html', reclamacoes=reclamacoes.all())


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


