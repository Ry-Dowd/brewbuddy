from .middlewares import login_required
from flask import Flask, json, g, request
from app.service import Service as Brew
from app.schema import BrewSchema
from flask_cors import CORS

app = Flask(__name__)