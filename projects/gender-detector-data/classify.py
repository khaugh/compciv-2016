import os
import csv
from gender import detect_gender

def extract_usable_name(firstname):
    return firstname

directory = 'tempdata'
subdirectory = 'legislator_data'
filename = 'wrangled_data.csv'
foldername = os.path.join(directory, subdirectory)
pathname = os.path.join(foldername, filename)

wrangledHeaders = ['title', 'first_name', 'last_name', 'party', 'age', 'gender', 'ratio', 'usable_name']

openFile = open(pathname, 'r')
print('Reading data from', pathname)

lineCount = 0
legislatorList = []
for line in openFile:
    if lineCount > 0:
        legislatorInfo = line.strip().split(',')
        firstname = extract_usable_name(legislatorInfo[1])
        genderInfo = detect_gender(firstname)
        infoDict = {}
        infoDict['title'] = legislatorInfo[0]
        infoDict['first_name'] = legislatorInfo[1]
        infoDict['last_name'] = legislatorInfo[2]
        infoDict['party'] = legislatorInfo[3]
        infoDict['age'] = legislatorInfo[4]
        infoDict['gender'] = genderInfo['gender']
        infoDict['ratio'] = genderInfo['ratio']
        infoDict['usable_name'] = firstname
        legislatorList.append(infoDict)
    lineCount += 1

newFileName = 'classified_data.csv'
newFilePath = os.path.join(foldername, newFileName)
csvFile = open(newFilePath, 'w')
writer = csv.DictWriter(csvFile, fieldnames=wrangledHeaders)
writer.writeheader()

for row in legislatorList:
    writer.writerow(row)

csvFile.close()
print('Successfully classified all data')