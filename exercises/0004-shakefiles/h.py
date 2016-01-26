import os
import glob

dirName = os.path.join('tempdata', '**', '*')
directories = glob.glob(dirName)


totalLines = 0
totalNonBlankLines = 0
for name in directories:
	openFile = open(name)
	lines = 0
	nonBlankLines = 0
	for line in openFile:
		lines += 1
		if len(line.strip()) is not 0:
			nonBlankLines += 1
	totalLines += lines
	totalNonBlankLines += nonBlankLines
	print(name, 'has', nonBlankLines, 'non-blank lines out of', lines, 'lines')
print('All together, Shakespeare''s 42 text files have:')
print(totalNonBlankLines, 'non-blank lines out of', totalLines, 'total lines')
