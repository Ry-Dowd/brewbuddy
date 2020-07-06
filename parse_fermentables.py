import json

def transform(fermentable):
  return{
    'name':fermentable['name'],
    'brand':fermentable['brand']
  }

output=[]

with open('fermentables.json', 'r+') as data:
  fermentables = json.load(data)

  output = [transform(fermentable) for fermentable in fermentables if (fermentable['brand'] and (fermentable['category'] in ['Grain', 'Adjunct']) or fermentable['category'] in ['Fruit', 'Sugar'])]

print(output)
with open ('parsed_fermentables.json', 'w') as f:
  json.dump(output, f, indent=2)