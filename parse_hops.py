import json

def transform(hop):
  return{
    'name':hop['name'],
    'alpha':hop['avgaa'],
    'description':hop['description'],
    'brand':hop['brand']
  }

output=[]

with open('hops.json', 'r+') as data:
  hops = json.load(data)

  output = [transform(hop) for hop in hops if hop['brand']]

print(output)
with open ('parsed_hops.json', 'w') as f:
  json.dump(output, f, indent=2)