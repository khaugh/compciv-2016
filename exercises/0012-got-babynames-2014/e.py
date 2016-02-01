namesFile = open('tempdata/ssa-babynames-nationwide-2014.txt', 'r')

girlCount = 0
boyCount = 0
for line in namesFile:
        name, sex, number = line.strip().split(',')
        if sex == 'F':
                girlCount += int(number)
        elif sex == 'M':
                boyCount += int(number)

namesFile.close()

print('F:', girlCount)
print('M:', boyCount)
