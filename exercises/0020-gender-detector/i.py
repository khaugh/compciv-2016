import os

directory = 'tempdata'
pathname = os.path.join(directory, 'wrangled2014.csv')

openFile = open(pathname, 'r')
openFile.readline()

count60 = 0
count70 = 0
count80 = 0
count90 = 0
count99 = 0
totalCount = 0

for line in openFile:
    year, name, gender, ratio, females, males, total = line.strip().split(',')
    if int(total) >= 100:
        totalCount += 1

        if int(ratio) <= 60:
            count60 += 1
        if int(ratio) <= 70:
            count70 += 1
        if int(ratio) <= 80:
            count80 += 1
        if int(ratio) <= 90:
            count90 += 1
        if int(ratio) <= 99:
            count99 += 1

print('Popular names in 2014 with gender ratio less than or equal to:')
print('  60%:', count60, '/', totalCount)
print('  70%:', count70, '/', totalCount)
print('  80%:', count80, '/', totalCount)
print('  90%:', count90, '/', totalCount)
print('  99%:', count99, '/', totalCount)