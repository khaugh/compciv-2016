import os
import requests
from shutil import unpack_archive
from glob import glob

url = 'https://www.ssa.gov/oact/babynames/names.zip'

directory = 'tempdata'
subdirectory = 'gender_data'
filename = 'names.zip'
pathname = os.path.join(directory, subdirectory, filename)

folderPath = os.path.join(directory, subdirectory)
if not os.path.exists(folderPath):
    os.makedirs(folderPath)

print('Downloading', url)
resp = requests.get(url)

openFile = open(pathname, 'wb')
openFile.write(resp.content)
openFile.close()

unpack_archive(pathname, extract_dir=folderPath)
fileNames = glob(os.path.join(folderPath, '*.txt'))

fileCount = 0
for file in fileNames:
    fileCount += 1

print('There are', fileCount, 'files')