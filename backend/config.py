from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

def get_env_variable(name):
    try:
        return environ[name]
    except KeyError:
        message = f"Expected environment variable '{name}' not set."
        raise Exception(message)

class Config:

  ENV = 'development'
  TESTING = True
  SECRET_KEY = environ.get('SECRET_KEY')
  STATIC_FOLDER = 'static'
  TEMPLATES_FOLDER = 'templates'

  # Database
  POSTGRES_URL = get_env_variable("POSTGRES_URL")
  POSTGRES_USER = get_env_variable("POSTGRES_USER")
  POSTGRES_PW = get_env_variable("POSTGRES_PW")
  POSTGRES_DB = get_env_variable("POSTGRES_DB")
  SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PW}@{POSTGRES_URL}/{POSTGRES_DB}"

class ProductionConfig(Config):
  FLASK_ENV = 'production'
  TESTING = False
  DEBUG = False
  DATABASE_URI = environ.get('PROD_DATABASE_URI')