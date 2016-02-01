import json
f = open('tempdata/googlemaps/stanford.json', 'r')
txt = f.read()
f.close()

mydict = json.loads(txt)
results = mydict["results"]

for i in range(0, len(results)):
        result = results[i]
        formatted_address = result["formatted_address"]
        lng = result["geometry"]["location"]["lng"]
        lat = result["geometry"]["location"]["lat"]
        print(formatted_address, lng, lat, sep=';')
