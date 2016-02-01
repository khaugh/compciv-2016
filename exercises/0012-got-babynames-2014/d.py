namesFile = open('tempdata/ssa-babynames-nationwide-2014.txt', 'r')

print('Top baby girl names')

girlCount = 0
boyCount = 0
for line in namesFile:
        name, sex, number = line.strip().split(',')
        if girlCount < 5:
                print(girlCount + 1, '.', name, number)
                girlCount += 1
        elif boyCount < 5 and sex == 'M':
                if boyCount == 0:
                        print('\nTop baby boy names')
                print(boyCount + 1, '.', name, number)
                boyCount += 1

namesFile.close()
