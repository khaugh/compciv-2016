import requests
import os

url = 'http://stash.compciv.org/scrapespeare/matty.shakespeare.tar.gz'
print('Downloading:', url)
resp = requests.get(url)

filename = os.path.join('tempdata', 'matty.shakespeare.tar.gz')
print('Writing file:', filename)
newfile = open(filename, "wb")
newfile.write(resp.content)
newfile.close()
