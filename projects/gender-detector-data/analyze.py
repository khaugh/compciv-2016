import os

directory = 'tempdata'
subdirectory = 'legislator_data'
filename = 'classified_data.csv'
foldername = os.path.join(directory, subdirectory)
pathname = os.path.join(foldername, filename)

openFile = open(pathname, 'r')
lineCount1 = 0
totalCounts = {'M': 0, 'F': 0, 'NA': 0}
for line in openFile:
    if lineCount1 > 0:
        title, first_name, last_name, party, age, gender, ratio, usable_name = line.strip().split(',')
        totalCounts[gender] += 1
    lineCount1 += 1

print('Males in Congress:', totalCounts['M'])
print('Females in Congress:', totalCounts['F'])
print('Unable to classify', totalCounts['NA'], 'records')
print('Percentage female:', round(totalCounts['F'] / (totalCounts['F'] + totalCounts['M']) * 100, 2), '%')

openFile = open(pathname, 'r')
lineCount2 = 0
countByParty = {'M': {'R':0, 'D':0, 'I':0}, 'F': {'R':0, 'D':0, 'I':0}, 'NA': {'R':0, 'D':0,'I':0}}
for line in openFile:
    if lineCount2 > 0:
        title, first_name, last_name, party, age, gender, ratio, usable_name = line.strip().split(',')
        countByParty[gender][party] += 1
    lineCount2 += 1


print()
print('Female party breakdown')
print('R: ', countByParty['F']['R'], ' (', round(countByParty['F']['R'] / totalCounts['F'] * 100, 2), '%)', sep="")
print('D: ', countByParty['F']['D'], ' (', round(countByParty['F']['D'] / totalCounts['F'] * 100, 2), '%)', sep="")
print('I: ', countByParty['F']['I'], ' (', round(countByParty['F']['I'] / totalCounts['F'] * 100, 2), '%)', sep="")
print()
print('Male party breakdown')
print('R: ', countByParty['M']['R'], ' (', round(countByParty['M']['R'] / totalCounts['M'] * 100, 2), '%)', sep="")
print('D: ', countByParty['M']['D'], ' (', round(countByParty['M']['D'] / totalCounts['M'] * 100, 2), '%)', sep="")
print('I: ', countByParty['M']['I'], ' (', round(countByParty['M']['I'] / totalCounts['M'] * 100, 2), '%)', sep="")


openFile = open(pathname, 'r')
lineCount3 = 0
totalAge = {'M':0, 'F':0, 'NA':0}
for line in openFile:
    if lineCount3 > 0:
        title, first_name, last_name, party, age, gender, ratio, usable_name = line.strip().split(',')
        totalAge[gender] += int(age)
    lineCount3 += 1

print()
print('Average female age:', round(totalAge['F'] / totalCounts['F']))
print('Average male age:', round(totalAge['M'] / totalCounts['M']))