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

for i in range(0, 10):
	print(i+1, ".", sep = "", end = " ")
	print(recordList[i][0], recordList[i][1], recordList[i][2], sep = ',')
