import re

namesFile = open('tempdata/ssa-babynames-nationwide-2014.txt')

daenerys = 0
khaleesi = 0
for line in namesFile:
        name, sex, number = line.strip().split(',')
        if name.strip() == "Daenerys":
                daenerys += int(number)
        elif re.match("Khale[es]s", name.strip()):
                khaleesi += int(number)

namesFile.close()

print('Daenerys:', daenerys)
print('Khaleesi:', khaleesi)
