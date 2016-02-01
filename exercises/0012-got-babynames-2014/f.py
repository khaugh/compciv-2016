import string

namesFile = open('tempdata/ssa-babynames-nationwide-2014.txt', 'r')

counts = {}
for line in namesFile:
        name, sex, count = line.strip().split(',')
        lastLetter = name[-1]
        if counts.get(lastLetter):
                counts[lastLetter] += int(count)
        else:
                counts[lastLetter] = int(count)

namesFile.close()

for char in string.ascii_lowercase:
        print(char, ':', counts[char])
