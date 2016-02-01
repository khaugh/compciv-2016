import string

namesFile = open('tempdata/ssa-babynames-nationwide-2014.txt', 'r')


counts = {'M': {}, 'F': {}}
for line in namesFile:
        name, sex, count = line.strip().split(',')
        lastLetter = name[-1]
        if counts.get(sex).get(lastLetter):
                counts[sex][lastLetter] += int(count)
        else:
                counts[sex][lastLetter] = int(count)

print('letter'.ljust(8), 'F'.rjust(8), 'M'.rjust(8))
print('------------------------')

for char in string.ascii_lowercase:
        print(char.ljust(8), str(counts['F'][char]).rjust(8), str(counts['M'][char]).rjust(8))
