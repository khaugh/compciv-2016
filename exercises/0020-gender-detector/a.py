import os
import requests
from shutil import unpack_archive
from glob import glob

url = 'https://www.ssa.gov/oact/babynames/names.zip'
pathname = os.path.join('tempdata', 'names.zip')

if not os.path.exists('tempdata'):
	os.makedirs('tempdata')

print('Downloading', url)
resp = requests.get(url)

openFile = open(pathname, 'wb')
openFile.write(resp.content)
openFile.close()

unpack_archive(pathname, extract_dir='tempdata')
fileNames = glob(os.path.join('tempdata', '*.txt'))

fileCount = 0
for file in fileNames:
	fileCount += 1

print('There are', fileCount, 'txt files')
