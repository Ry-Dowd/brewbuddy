from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional

class SignupForm(FlaskForm):
  username=StringField('Username', validators=[DataRequired()])
  email=StringField('Email', validators=[Length(min=6), Email(message='Enter a valid email.'), DataRequired()])
  password=PasswordField('Password', validators=[DataRequired(), Length(min=8, message='Select a stronger password')])
  confirm=PasswordField('Confirm Your Password', validators=[DataRequired(), EqualTo('password', message='Password must match.')])
  submit=SubmitField('Register')

class LoginForm(FlaskForm):
  email=StringField('Email', validators=[DataRequired(), Email(message='Enter a Valid Email.')])
  password=PasswordField('Password', validators=[DataRequired()])
  submit=SubmitField('Login')