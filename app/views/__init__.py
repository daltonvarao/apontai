from .index import index_bp
from .login import login_bp
from .cadastro import cadastro_bp
from .reclamacao import reclamacao_bp
from .sobre import sobre_bp


def register_all_blueprints(app):
    app.register_blueprint(index_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(cadastro_bp)
    app.register_blueprint(reclamacao_bp)
    app.register_blueprint(sobre_bp)
