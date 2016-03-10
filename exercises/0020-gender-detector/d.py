import os
from glob import glob

directory = 'tempdata'
pathname = os.path.join(directory, '*.txt')
textFiles = glob(pathname)

for file in textFiles:
        basename = os.path.basename(file)
        year = int(basename[-8:-4])
        if year >= 1950:
                uniqueNames = {'M': set(), 'F': set()}
                filePath = os.path.join(directory, basename)
                openFile = open(filePath, 'r')
                for line in openFile:
                        name, sex, count = line.strip().split(',')
                        uniqueNames[sex].add(name)
                uniqueGirls = len(uniqueNames['F'])
                uniqueBoys = len(uniqueNames['M'])
                ratio = round(uniqueGirls / uniqueBoys * 100)
                print(year)
                print('F:', str(uniqueGirls).rjust(6), 'M:', str(uniqueBoys).rjust(6))
                print('F/M name ratio:', ratio)
                openFile.close()

