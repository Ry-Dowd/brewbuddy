import os
from flask_sqlalchemy import SQLAlchemy
from . import config
from flask import Flask
from . import endpoints
from . import auth
from models import db

db=SQLAlchemy()

def create_app(test_config=None):
  app = Flask(__name__, instance_relative_config=True)

  if test_config is None:
    app.config.from_object(config.Config)
  else:
    app.config.from_mapping(test_config)


  try:
    os.makedirs(app.instance_path)
  except OSError:
    pass
  
  db.init_app(app)

  with app.app_context():

    db.create_all()

    app.register_blueprint(endpoints.bp)
    app.register_blueprint(auth.bp)

    @app.route('/hello')
    def hello():
      return "Hello, World!"

    return app