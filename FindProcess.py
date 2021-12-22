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
    dstDict = LoadTraitTxtToDict("AntivirusProcess.txt")

    try:
        srcFile = open(sys.argv[1], 'r')
    except:
        print("File is not accessible.")

    while True:
        procLine = srcFile.readline()
        if procLine == '':
            break

        index = procLine.find(' ')
        key = procLine[:index]

        if '.exe' not in key.lower():
            continue

        if dstDict.__contains__(key):
            print('%d %s %s' % (i, key, dstDict[key]))
            i += 1

    if i == 0:
        print('We don\'t find any Antivirus process! ')