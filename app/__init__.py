import os
from flask import Flask
<<<<<<< HEAD
from flask_migrate import Migrate
from app.views.home import home_bp
from app.models import models
=======
from app.views.index import index_bp
from flask_migrate import Migrate, MigrateCommand
from app.models.db import db
>>>>>>> 3133a2d4f9d9333da950f57233074bfb2fda1e01


def create_app():

    app = Flask(__name__,
                static_url_path='',
                static_folder='static')
<<<<<<< HEAD
    
    app.config.from_object('config')
    app.register_blueprint(home_bp)
    
    db = models.db
    db.init_app(app)
    
    migrate = Migrate(app, db)
=======

    app.config.from_object('config')
    
    app.register_blueprint(index_bp)

    db.init_app(app)

    migrate = Migrate(app, db)

>>>>>>> 3133a2d4f9d9333da950f57233074bfb2fda1e01
    return app
