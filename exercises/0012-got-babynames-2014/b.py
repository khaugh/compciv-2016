namesFile = open('tempdata/ssa-babynames-nationwide-2014.txt', 'r')

sum = 0
for line in namesFile:
        strs = line.split(',')
        sum += int(strs[2])

namesFile.close()

print('There are', sum, 'babies whose names were recorded in 2014.')
