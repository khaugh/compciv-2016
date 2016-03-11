import os

def findName(inputName):
    openFile = open(pathname, 'r')
    for line in openFile:
        name, gender, ratio, females, males, total = line.strip().split(',')
        if inputName.lower() == name.lower():
            return {'name': inputName, 'gender': gender, 'ratio': int(ratio), 'females': int(females), 'males': int(males), 'total': int(total)}

    openFile.close()
    return {'name': inputName, 'gender': 'NA', 'ratio': None, 'females': None, 'males': None, 'total': 0}


toSearch = ['Michael', 'Kelly', 'Kanye', 'THOR', 'casey', 'Arya', 'ZZZblahblah']

directory = 'tempdata'
pathname = os.path.join(directory, 'wrangledbabynames.csv')

femaleCount = 0
maleCount = 0
NACount = 0

totalMales = 0
totalFemales = 0

for inputName in toSearch:
    nameDict = findName(inputName)

    if nameDict['gender'] == 'F':
        femaleCount += 1
        totalFemales += nameDict['females']
        totalMales += nameDict['males']
    elif nameDict['gender'] == 'M':
        maleCount += 1
        totalFemales += nameDict['females']
        totalMales += nameDict['males']
    else:
        NACount += 1

    print(inputName, nameDict['gender'], nameDict['ratio'])
        
print('F:', femaleCount, 'M:', maleCount, 'NA:', NACount)
print('females:', totalFemales, 'males:', totalMales)