from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    senha = db.Column(db.String(100))

    def first_name(self):
        return self.nome.split(' ')[0]
    
    reclamacoes = db.relationship('Reclamacao', back_populates='usuario')


class Reclamacao(db.Model):
    __tablename__ = 'reclamacao'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(60))
    tipo = db.Column(db.String(100))
    local = db.Column(db.String(100))
    descricao = db.Column(db.String(500))
    img_url = db.Column(db.String(500))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    fechado = db.Column(db.Boolean, default=False)
    usuario = db.relationship('Usuario', back_populates="reclamacoes")
    reclamadores = db.relationship('Usuario', secondary="usuario_reclamacao")
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)


UsuarioReclamacao = db.Table('usuario_reclamacao', db.Model.metadata,
    db.Column('usuario_id', db.Integer, db.ForeignKey('usuario.id')),
    db.Column('reclamacao_id', db.Integer, db.ForeignKey('reclamacao.id'))
)
