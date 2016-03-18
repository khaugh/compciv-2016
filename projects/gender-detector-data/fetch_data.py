import os
import requests

url = 'http://unitedstates.sunlightfoundation.com/legislators/legislators.csv'

directory = 'tempdata'
subdirectory = 'legislator_data'
filename = 'legislators.csv'
folderName = os.path.join(directory, subdirectory)
pathname = os.path.join(folderName, filename)

if not os.path.exists(folderName):
    os.makedirs(folderName)

print('Downloading', url)
resp = requests.get(url)

openFile = open(pathname, 'w')
openFile.write(resp.text)
openFile.close()
