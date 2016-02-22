import requests
import os

if not os.path.exists('tempdata'):
        os.makedirs('tempdata')

url = 'http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt'
resp = requests.get(url)

pathname = os.path.join('tempdata', os.path.basename(url))
openFile = open(pathname, "w")
openFile.write(resp.text)
openFile.close()

print('There are', len(resp.text), 'characters in', pathname)

