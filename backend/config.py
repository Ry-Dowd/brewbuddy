from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:

  FLASK_ENV = 'development'
  TESTING = True
  SECRET_KEY = environ.get('SECRET_KEY')
  STATIC_FOLDER = 'static'
  TEMPLATES_FOLDER = 'templates'

  # Database
  MONGO_URI = "mongodb://mongo_user:secret@localhost:27017"

class ProductionConfig(Config):
  FLASK_ENV = 'production'
  TESTING = False
  DEBUG = False
  DATABASE_URI = environ.get('PROD_DATABASE_URI')