from os.path import join

def sortByLength(item):
	return (len(item[0]), item[1])	

fileName = join('tempdata', 'ssa-babynames-nationwide-2014.txt')
openFile = open(fileName, 'r')

namesDict = {}
for line in openFile:
	name, sex, count = line.strip().split(',')
	if namesDict.get(name):
		namesDict[name] += int(count)
	else:
		namesDict[name] = int(count)

filteredNamesDict = {}
for key in namesDict:
	if namesDict[key] > 2000:
		filteredNamesDict[key] = namesDict[key]

sortedList = sorted(filteredNamesDict.items(), key = sortByLength, reverse = True)

for i in range(0,10):
	print(sortedList[i][0].ljust(len(sortedList[0][0]) + 5), sortedList[i][1])
