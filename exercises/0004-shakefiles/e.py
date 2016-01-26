import os

filename = 'tempdata/tragedies/hamlet'
hamletFile = open(filename)

x = 0
for line in hamletFile:
     x += 1

print(filename, 'has', x, 'lines')   
hamletFile.close()
