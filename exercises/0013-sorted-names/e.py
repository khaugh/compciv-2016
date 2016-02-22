from os.path import join
from operator import itemgetter

fileName = join('tempdata', 'ssa-babynames-nationwide-2014.txt')
openFile = open(fileName, 'r')

recordList = []
for line in openFile:
        name, sex, count = line.strip().split(",")
        record = [name, sex, int(count)]
        recordList.append(record)

recordList.sort(key = itemgetter(2), reverse = True)

to10count = 0
to100count = 0
to1000count = 0
to10000count = 0
past10000count = 0

lineCount = 1
totalCount = 0
for name, sex, count in recordList:
	if lineCount <= 10:
		to10count += int(count)
	elif lineCount <= 100:
		to100count += int(count)
	elif lineCount <= 1000:
		to1000count += int(count)
	elif lineCount <= 10000:
		to10000count += int(count)
	else:
		past10000count += int(count)
	totalCount += int(count)
	lineCount += 1

#print(to10count)
#print(to100count)

print('Names 1 to 10:', round(to10count/totalCount * 100, 1))
print('Names 11 to 100:', round(to100count/totalCount * 100, 1))
print('Names 101 to 1000:', round(to1000count/totalCount * 100, 1))
print('Names 1001 to 10000:', round(to10000count/totalCount * 100, 1))
print('Names 10001 to', lineCount - 1, ':', round(past10000count/totalCount * 100, 1))
