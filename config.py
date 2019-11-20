import os


class Config:
    CSRF_ENABLED = True
    SECRET_KEY = 'your-very-very-secret-key'
    SQLALCHEMY_DATABASE_URI = 'postgresql:///flask_template_dev'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


class Development(Config):
    ENV = 'development'
    DEBUG = True
    TESTING = False


class Production(Config):
    ENV = 'production'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgres://firhokdcdnfygz:93231d3f2ae1156cabfc40f7e4ba08587a77f68a5e2072fbcbbdb30150ba4bcb@ec2-107-22-253-158.compute-1.amazonaws.com:5432/df9c5vvl0s21da')
