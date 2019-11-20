import os
from flask_script import Manager, Server
from flask_migrate import MigrateCommand
from app import create_app
from app.models.db import db


def set_app_mode(env):
    return 'config.Development' if env == 'development' else 'config.Production'


if __name__ == '__main__':
    app_mode = set_app_mode(os.getenv('APP_MODE', 'development'))

    app = create_app(app_mode)
    port = os.getenv('PORT', 5000)

    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    manager.add_command('runserver', Server(host='0.0.0.0', port=port))
    manager.run()
