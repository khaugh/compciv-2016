from os.path import join, basename

directory = 'tempdata'
thefilename = join(directory, 'yob2014.txt')

names = {}
thefile =  open(thefilename, 'r')
for line in thefile:
    name, gender, count = line.split(',')
    if not names.get(name):
        names[name] = {'M': 0, 'F': 0}
    names[name][gender] += int(count)
thefile.close()

totalUniqueCount = len(names)
totalOverallCount = 0
for name in names:
        totalOverallCount += names[name]['M'] + names[name]['F']
print("Total:", totalUniqueCount, "unique names for", totalOverallCount, "babies")


for gender in ['M', 'F']:
        totalGenderCount = 0
        totalGenderUnique = 0
        for v in names.values():
                if v[gender] > 0:
                        totalGenderCount += v[gender]
                        totalGenderUnique += 1
        print("    %s:" %gender, totalGenderUnique, "unique names for", totalGenderCount, "babies")
