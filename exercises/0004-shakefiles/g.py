import os
import glob

dirName = os.path.join('tempdata','tragedies', '*')
files = glob.glob(dirName)

for fileName in files:
	openFile = open(fileName)
	totalLines = 0
	for line in openFile:
		totalLines += 1
	openFile.close()
	
	print(fileName, 'has', totalLines, 'lines')
	
	openFile = open(fileName)
	for x in range(totalLines):
		line = openFile.readline()
		if x >= totalLines -5:
			print(x + 1, ':', line.strip())
	openFile.close()

