from flask_sqlalchemy import SQLAlchemy
import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
  if 'db' not in g:
    g.db = SQLAlchemy(current_app)
  return g.db

def close_db(e=none):
  db = g.pop('db', None)

  if db is not None:
    db.close()