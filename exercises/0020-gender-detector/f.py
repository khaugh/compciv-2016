import os
from glob import glob

startYear = 1950
endYear = 2015

for fifthYear in range(startYear, endYear, 5):
        total = 0
        names = {}
        pathname = os.path.join('tempdata', 'yob' + str(fifthYear) + '.txt')
        if os.path.exists(pathname):
                openFile = open(pathname, 'r')
        for line in openFile:
                name, gender, count = line.strip().split(',')
                if not names.get(name):
                        names[name] = {'M': 0, 'F': 0}
                names[name][gender] += int(count)
                total += int(count)
        unique = len(names.keys())
        print(fifthYear)
        print('Total:', str(round(total/unique)), "babies per name")
        
        for gender in ['M', 'F']:
                totalGender = 0
                uniqueGender = 0
                for v in names.values():
                        if v[gender] > 0:
                                totalGender += v[gender]
                                uniqueGender += 1
                print("    %s:" %gender, round(totalGender / uniqueGender), 'babies per name')
                        
