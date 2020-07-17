from flask import Blueprint, render_template, request, flash, session, url_for, redirect
from flask_login import login_required, logout_user, current_user, login_user
from .forms import SignupForm, LoginForm
from .models import db, User
from . import login_manager

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
    return redirect('/hello')
  form=LoginForm()
  if form.validate_on_submit():
    user=User.query.filter_by(email=form.email.data).first()
    if user and user.check_password(password=form.password.data):
      login_user(user)
      return redirect('/hello')
    flash('Invalid username/password combination')
    return redirect('/auth/login')
  return render_template('login.html', form=form, title='Log in')

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
  form=SignupForm()
  if form.validate_on_submit():
    existing_user=User.query.filter_by(email=form.email.data).first()
    if existing_user is None:
      user=User(username=form.username.data, email=form.email.data)
      user.set_password(form.password.data)
      db.session.add(user)
      db.session.commit()
      login_user(user)
      return redirect(url_for('hello'))
  return render_template('signup.html', title='Create Account', form=form, template='signup-page', body='Sign up for BrewBuddy.')

@bp.route('/logout')
def logout():
  return 'logout'

@login_manager.user_loader
def load_user(user_id):
  if user_id is not None:
    return User.query.get(user_id)
  return None

@login_manager.unauthorized_handler
def unauthorized():
  flash('You must be logged in to view that page.')
  return redirect(url_for('login'))