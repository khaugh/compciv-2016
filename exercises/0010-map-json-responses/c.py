import json
f = open('tempdata/googlemaps/stanford.json', 'r')
txt = f.read()
f.close()

mydict = json.loads(txt)
results = mydict["results"]

for i in range(0, len(results)):
	result = results[i]
	print(result["formatted_address"])
