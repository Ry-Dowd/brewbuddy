from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), index=False, nullable=False)
  email = db.Column(db.String(64), unique=True, nullable=False)
  password = db.Column(db.String(200), primary_key=False, unique=False, nullable=False)
  beers = db.relationship('Beer', backref='user', lazy=True)

  def set_password(self, password):
    self.password = generate_password_hash(password, method='sha256')

  def check_password(self, password):
    return check_password_hash(self.password, password)

  def __repr__(self):
    return f'<User {self.username}'

class Beer(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(40), index=False, nullable=False)
  author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  recipe = db.Column(db.JSON)