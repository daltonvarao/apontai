from .db import db


class Reclamacao(db.Model):
    __tablename__ = 'reclamacao'

    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(100))
    local = db.Column(db.String(100))
    tempo = db.Column(db.String(50))
    desc = db.Column(db.String(500))
    img_url = db.Column(db.String(500))
