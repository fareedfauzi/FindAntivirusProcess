import os
import sys


def LoadTraitTxtToDict(FilePath):
    try:
        File = open(FilePath, 'r')
    except IOError:
        print("File is not accessible.")

    txtDict = {} #create Dict

    while True:
        line = File.readline()
        if line == '':
            break

        index = line.find('|')
        key = line[:index]
        value = line[index+1:]
        txtDict[key] = value[:-1]

    File.close()
    return txtDict




if __name__=="__main__":
    i = 0
    dstDict = LoadTraitTxtToDict("AntivirusServices.txt")
    

# Remove word
    srcFile = open(sys.argv[1], 'r')
    remove_word = "SERVICE_NAME: "
    lst = []
    for line in srcFile:
        if remove_word in line:
            line = line.replace(remove_word,"")
        lst.append(line)
    srcFile.close()

    srcFile = open(sys.argv[1], 'w')
    for line in lst:
        srcFile.write(line)
    srcFile.close()

# Searching
    srcFile = open(sys.argv[1], 'r')
    while True:
        proLine = srcFile.readline()
        if proLine == '':
            break

        index = proLine.find(' ')
        key = proLine[:index]

        if dstDict.__contains__(key):
            print('%d %s %s' % (i, key, dstDict[key]))
            i += 1

    if i == 0:
        print('We don\'t find any Antivirus services! ')