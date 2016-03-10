import os
from glob import glob

directory = 'tempdata'
pathname = os.path.join(directory, '*.txt')
textFiles = glob(pathname)

boyCount = 0
girlCount = 0
for file in textFiles:
	basename = os.path.basename(file)
	year = int(basename[-8:-4])
	if year >= 1950:
		filePath = os.path.join(directory, basename)
		openFile = open(filePath, 'r')
		for line in openFile:
			name, sex, count = line.strip().split(',')
			if sex == 'M':
				boyCount += int(count)
			else:
				girlCount += int(count)
                openFile.close()

print('F:', str(girlCount).rjust(6), 'M:', str(boyCount).rjust(6))

ratio = round(girlCount / boyCount * 100)
print('F/M baby ratio:', ratio)
