import requests
import os

if not os.path.exists('tempdata'):
        os.makedirs('tempdata')
if not os.path.exists('tempdata/googlemaps'):
	os.makedirs('tempdata/googlemaps')
if not os.path.exists('tempdata/mapzen'):
	os.makedirs('tempdata/mapzen')

url1 = 'http://www.compciv.org/files/datadumps/apis/googlemaps/geocode-stanford.json'
url2 = 'http://www.compciv.org/files/datadumps/apis/mapzen/search-stanford.json'

print('---')
print('Downloading from:', url1)
googlemaps = requests.get(url1)

filename1 = os.path.join('tempdata', 'googlemaps', 'stanford.json')
googleFile = open(filename1, "w")
print('Writing to:', filename1)
googleFile.write(googlemaps.text)
googleFile.close()

numGoogleChars = len(googlemaps.text)
numGoogleLines = len(googlemaps.text.splitlines())

print('Wrote', numGoogleLines, 'lines and', numGoogleChars, 'characters')


print('---')
print('Downloading from:', url2)
mapzen = requests.get(url2)

filename2 = os.path.join('tempdata', 'mapzen', 'stanford.json')
mapzenFile = open(filename2, "w")
print('Writing to:', filename2)
mapzenFile.write(mapzen.text)
mapzenFile.close()

numMapzenChars = len(mapzen.text)
numMapzenLines = len(mapzen.text.splitlines())

print('Wrote', numMapzenLines, 'lines and', numMapzenChars, 'characters')
