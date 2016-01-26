import os

filename = 'tempdata/tragedies/hamlet'
hamletFile = open(filename)

for x in range(5):
	print(hamletFile.readline().strip())
hamletFile.close()
