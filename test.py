import re

reObj = re.compile(r'\w.*')

def functionRead(filePointer):
    fileString = filePointer.read()
    if reObj.search(fileString):
        print("found something")
    else:
        print("Nothing i think so")

    #print(fileString )
    del fileString

filePointer = open("textFile.txt", 'r')
functionRead(filePointer)

