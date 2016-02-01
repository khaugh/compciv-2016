import json
f = open('tempdata/mapzen/stanford.json', 'r')
txt = f.read()
f.close()

mydict = json.loads(txt)

print('type:', mydict["type"])
print('text:', mydict["geocoding"]["query"]["text"])
print('size:', mydict["geocoding"]["query"]["size"])
print('boundary.country:', mydict["geocoding"]["query"]["boundary.country"])

