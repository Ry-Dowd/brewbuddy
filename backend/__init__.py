import os

from . import config
from flask import Flask
from flask_pymongo import PyMongo
from . import endpoints
from . import auth

mongo = PyMongo()

def create_app(test_config=None):
  app = Flask(__name__, instance_relative_config=True)

  if test_config is None:
    app.config.from_object(config.Config)
  else:
    app.config.from_mapping(test_config)

  print("config:", app.config)
  mongo.init_app(app)

  try:
    os.makedirs(app.instance_path)
  except OSError:
    pass
  
  app.register_blueprint(endpoints.bp)
  app.register_blueprint(auth.bp)

  @app.route('/hello')
  def hello():
    return "Hello, World!"

  return app