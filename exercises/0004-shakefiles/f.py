import os

filename = 'tempdata/tragedies/romeoandjuliet'
romeoFile = open(filename)
totalLines = 4766

for x in range(totalLines):
	line = romeoFile.readline()
	if x >= totalLines - 5:
		print(x, ':', line.strip())

romeoFile.close()
