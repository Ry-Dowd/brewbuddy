from .middlewares import login_required
from flask import Flask, json, g, request
from app.service import Service as Brew
from app.schema import BrewSchema
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/ping", methods=["GET"])
def pong():
  return json_response({})

@app.route("/brews", methods=["GET"])
@login_required
def index():
  return json_response(Brew(g.user).find_all_brews())

@app.route("/brews", methods=["POST"])
@login_required
def create():
  brew = BrewSchema().load(json.loads(request.data))

  if brew.errors:
    return json_response({'error':brew.errors}, 422)

  brew = Brew(g.user).create_brew_for(brew)
  return json_response(brew)

@app.route("/brew/<int:brew_id>", methods=["GET"])
@login_required
def show(brew_id):
  brew = Brew(g.user).find_brew(brew_id)

  if brew:
    return json_response(brew)
  else:
    return json_response({'error':'beer not found'})

@app.route("/brew/<int:brew_id>", methods=["POST"])
@login_required
def update(brew_id):
  brew = BrewSchema().load(json.loads(request.data))

  if brew.errors:
    return json_response({'error':brew.errors})

  brew_service = Brew(g.user)
  if brew_service.update_brew_with(brew_id, brew):
    return json_response(brew.data)
  else:
    return json_response({'error':'beer not found'}, 404)

@app.route("/brew/<int:brew_id>", methods=["DELETE"])
@login_required
def delete(brew_id):
  brew_service = Brew(g.user)
  if brew_service.delete_brew_for(brew_id):
    return json_response({})
  else:
    return json_response({'error':'beer not found'}, 404)

def json_response(payload, status=200):
  return (json.dumps(payload), status, {'content-type':'application/json'})
  