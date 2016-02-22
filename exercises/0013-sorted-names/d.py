from os.path import join

def byCount(item):
	return (item[1], item[0])

fileName = join('tempdata', 'ssa-babynames-nationwide-2014.txt')
openFile = open(fileName, 'r')

xMaleNames = []
xFemaleNames = []
for line in openFile:
	name, sex, count = line.strip().split(",")
	row = [name, int(count)]
	if 'x' in name.lower():
		if sex == 'M':
			xMaleNames.append(row)
		else:
			xFemaleNames.append(row)

xMaleNames.sort(key = byCount, reverse = True)

print('Female')
for i in range(0,5):
	print(i+1, ".", sep = "", end = " ")
	print(xFemaleNames[i][0].ljust(20), str(xFemaleNames[i][1]).rjust(5))

print('Male')
for i in range(0,5):
	print(i+1, ".", sep = "", end = " ")
	print(xMaleNames[i][0].ljust(20), str(xMaleNames[i][1]).rjust(5))
