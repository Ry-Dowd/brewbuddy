import json

def transform(yeast):
  return{
    'name':yeast['name'],
    'brand':yeast['brand'],
    'temprange': f"{yeast['mintemp']} - {yeast['maxtemp']}"
  }

output=[]

with open('yeasts.json', 'r+') as data:
  yeasts = json.load(data)

  output = [transform(yeast) for yeast in yeasts if yeast['brand']]

with open ('parsed_yeasts.json', 'w') as f:
  json.dump(output, f, indent=2)