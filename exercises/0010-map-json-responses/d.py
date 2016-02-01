import json
f = open('tempdata/googlemaps/stanford.json', 'r')
txt = f.read()
f.close()

mydict = json.loads(txt)
results = mydict["results"]

for i in range(0, len(results)):
        result = results[i]
        address_components = result["address_components"]
        for j in range(0, len(address_components)):
                print(address_components[j]["long_name"], end='; ')
        print()

