from marshmallow import Schema, fields

class BrewSchema(Schema):
  
  brew_id = fields.Int(required=True)
  author = fields.String()
  author_id = fields.Email(required=True)
  fermentables = fields.Dict()
  hops = fields.Dict()
  miscs = fields.Dict()
  yeasts = fields.Dict()
  waters = fields.Dict()
  mash_steps = fields.Dict()
  fermentation_steps = fields.Dict()
  batch_size = fields.String()
  notes = fields.String()

class ReminderSchema(Schema):
  pass

class UserSchema(Schema):
  id = fields.Int(required=True)
  user_id = fields.Email(required=True)
  favorites = fields.List(fields.Int())

