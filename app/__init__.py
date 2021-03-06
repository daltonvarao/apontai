import os
from flask import Flask
from flask_migrate import Migrate
from app import views
from app.models import models


def create_app(app_mode):

    app = Flask(__name__,
                static_url_path='',
                static_folder='static')
    
    app.config.from_object(app_mode)
    views.register_all_blueprints(app)
    models.db.init_app(app)
    migrate = Migrate(app, models.db)
    
    return app
