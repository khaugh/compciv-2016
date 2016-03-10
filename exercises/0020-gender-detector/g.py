import os
import csv

def sortNames(dict):
    return (-dict['total'], dict['name'])


startYear = 1950
endYear = 2014

directory = 'tempdata'
wrangledHeaders = ['year', 'name', 'gender' , 'ratio' , 'females', 'males', 'total']
wrangledPathname = os.path.join(directory, 'wrangledbabynames.csv')


years = list(range(startYear, endYear, 10))
years.append(endYear)

for year in years:
    sourcePathname = os.path.join(directory, 'yob' + str(year) + '.txt')
    openFile = open(sourcePathname, 'r')
    
    names = {}
    for line in openFile:
        name, gender, count = line.strip().split(',')
        if not names.get(name):
            names[name] = {'M' : 0, 'F' : 0}
        names[name][gender] += int(count)
    
    openFile.close()
    
    nameList = []
    for name, counts in names.items():
        nameData = {}
        nameData['year'] = year
        nameData['name'] = name
        nameData['females'] = counts['F']
        nameData['males'] = counts['M']
        nameData['total'] = nameData['males'] + nameData['females']
        if nameData['females'] >= nameData['males']:
            nameData['gender'] = 'F'
            nameData['ratio'] = round(100 * nameData['females'] / nameData['total'])
        else:
            nameData['gender'] = 'M'
            nameData['ratio'] = round(100 * nameData['males'] / nameData['total'])
    
        nameList.append(nameData)

nameList.sort(key=sortNames)

csvFile = open(wrangledPathname, 'w')
writer = csv.DictWriter(csvFile, fieldnames=wrangledHeaders)
writer.writeheader()

for row in nameList:
    writer.writerow(row)

csvFile.close() 

finalFile = open(wrangledPathname, 'r')
for i in range(0, 5):
    line = finalFile.readline()
    print(line.strip())