import os
import csv
import datetime

def cleanLine(line):
    for i in range(0, 8):
        line = line.replace(',,', ', ,')
    return line

def dobToAge(birthdate):
    monthDayYear = birthdate.strip().split('-')
    year = monthDayYear[0]
    age = round(2016 - int(year))
    return age

directory = 'tempdata'
subdirectory = 'legislator_data'
filename = 'legislators.csv'
foldername = os.path.join(directory, subdirectory)
pathname = os.path.join(foldername, filename)

wrangledHeaders = ['title', 'first_name', 'last_name', 'party', 'age']

openFile = open(pathname, 'r')
print('Reading data from', pathname)

lineCount = 0
newLineCount = 0
legislatorList = []
for line in openFile:
    if (lineCount > 0):
        cleanline = cleanLine(line)
        infoList = cleanline.strip().split(',')
        inOffice = int(infoList[9])
        if inOffice == 1:
            infoDict = {}
            infoDict['title'] = infoList[0]
            infoDict['first_name'] = infoList[1]
            infoDict['last_name'] = infoList[3]
            infoDict['party'] = infoList[6]
            infoDict['age'] = dobToAge(infoList[27])
            legislatorList.append(infoDict)
            newLineCount += 1
    lineCount += 1

newFileName = 'wrangled_data.csv'
newFilePath = os.path.join(foldername, newFileName)
csvFile = open(newFilePath, 'w')
writer = csv.DictWriter(csvFile, fieldnames=wrangledHeaders)
writer.writeheader()

for row in legislatorList:
    writer.writerow(row)

csvFile.close()

print('Added', newLineCount, 'entries to', newFileName)