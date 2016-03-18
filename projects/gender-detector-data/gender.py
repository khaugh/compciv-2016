import os 

def detect_gender(inputName):
    directory = 'tempdata'
    subdirectory = 'gender_data'
    filename = 'wrangledbabynames.csv'
    pathname = os.path.join(directory, subdirectory, filename)

    openFile = open(pathname, 'r')
    for line in openFile:
        name, gender, ratio, females, males, total = line.strip().split(',')
        if inputName.lower() == name.lower():
            return {'name': inputName, 'gender': gender, 'ratio': int(ratio), 'females': int(females), 'males': int(males), 'total': int(total)}

    openFile.close()
    return {'name': inputName, 'gender': 'NA', 'ratio': None, 'females': None, 'males': None, 'total': 0}