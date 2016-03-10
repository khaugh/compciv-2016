import os

directory = 'tempdata'
pathname = os.path.join(directory, 'wrangled2014.csv')

openFile = open(pathname, 'r')
openFile.readline()

print('Most popular names with <= 60% gender skew:')
count = 0
for line in openFile:
    year, name, gender, ratio, females, males, total = line.strip().split(',')
    if int(ratio) <= 60:
        print(name.ljust(10), gender, ratio, total)
        count += 1
    if count >= 5:
        break