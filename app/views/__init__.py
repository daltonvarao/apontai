from .index import index_bp
from .login import login_bp

def register_all_blueprints(app):
    app.register_blueprint(index_bp)
    app.register_blueprint(login_bp)


