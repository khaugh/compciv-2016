import os
import csv

def condense(list):
    newList = []

    for i in range(len(list) - 1):
        newEntry = list[i]
        for j in range(i+1, len(list) - 1):
            if newEntry['name'] == list[j]['name']:
                newEntry['females'] += list[j]['females']
                newEntry['males'] += list[j]['males']
                newEntry['total'] += list[j]['total']
                if newEntry['females'] >= newEntry['males']:
                    newEntry['gender'] = 'F'
                    newEntry['ratio'] = round(100 * newEntry['females'] / newEntry['total'])
                else:
                    newEntry['gender'] = 'M'
                    newEntry['ratio'] = round(100 * newEntry['males'] / newEntry['total'])
        newList.append(newEntry)

    return newList


def condense(oldList):
    newList = []
    newList.append(oldList[0])
    newIndex = 0

    for oldIndex in range(len(oldList)):
        if newList[newIndex]['name'] == oldList[oldIndex]['name']:
            newList[newIndex]['females'] += oldList[oldIndex]['females']
            newList[newIndex]['males'] += oldList[oldIndex]['males']
            newList[newIndex]['total'] += oldList[oldIndex]['total']
            if newList[newIndex]['females'] >= newList[newIndex]['males']:
                newList[newIndex]['gender'] = 'F'
                newList[newIndex]['ratio'] = round(100 * newList[newIndex]['females'] / newList[newIndex]['total'])
            else:
                newList[newIndex]['gender'] = 'M'
                newList[newIndex]['ratio'] = round(100 * newList[newIndex]['males'] / newList[newIndex]['total'])
        else:
            newEntry = {}

            newEntry['name'] = oldList[oldIndex]['name']
            newEntry['females'] = oldList[oldIndex]['females']
            newEntry['males'] = oldList[oldIndex]['males']
            newEntry['total'] = oldList[oldIndex]['total']
            if newEntry['females'] >= newEntry['males']:
                newEntry['gender'] = 'F'
                newEntry['ratio'] = round(100 * newEntry['females'] / newEntry['total'])
            else:
                newEntry['gender'] = 'M'
                newEntry['ratio'] = round(100 * newEntry['males'] / newEntry['total'])

            newList.append(newEntry)
            newIndex += 1

    return newList

def sortByName(dict):
    return (dict['name'], -dict['total'])

def sortByTotal(dict):
    return (-dict['total'], dict['name'])


startYear = 1950
endYear = 2014

directory = 'tempdata'
wrangledHeaders = ['name', 'gender' , 'ratio' , 'females', 'males', 'total']
wrangledPathname = os.path.join(directory, 'wrangledbabynames.csv')


years = list(range(startYear, endYear, 10))
years.append(endYear)

nameList = []
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
    
    for name, counts in names.items():
        nameData = {}
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

nameList.sort(key=sortByName)
nameList = condense(nameList)
nameList.sort(key=sortByTotal)

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