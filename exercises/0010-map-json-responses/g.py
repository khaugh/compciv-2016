import json
f = open('tempdata/mapzen/stanford.json', 'r')
txt = f.read()
f.close()

mydict = json.loads(txt)
features = mydict["features"]

for f in features:
        properties = f["properties"]
        coordinates = f["geometry"]["coordinates"]
        print(properties["label"], properties["confidence"], coordinates[0], coordinates[1], end=';')
        print()
