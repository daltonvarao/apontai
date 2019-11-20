<<<<<<< HEAD
from flask_script import Manager, Server
from flask_migrate import MigrateCommand
from app import create_app
import os


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app = create_app()

    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    manager.add_command('runserver', Server(host="0.0.0.0", port=port))
    manager.run()
=======
import os
from flask_script import Manager, Server
from flask_migrate import MigrateCommand
from app import create_app
from app.models.db import db


if __name__ == '__main__':
    app = create_app()
    port = os.getenv('PORT', 5000)

    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    manager.add_command('runserver', Server(host='0.0.0.0', port=port))
    manager.run()
>>>>>>> 3133a2d4f9d9333da950f57233074bfb2fda1e01
