from .db import db


class Usuario(db.Model):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20))
    email = db.Column(db.String(20))
    senha = db.Column(db.String(50))
    # email = db.relationship('Article', backref='author', lazy=True)


# class Article(db.Model):
#     __tablename__ = 'article'

#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(50))
#     content = db.Column(db.Text)
#     author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
