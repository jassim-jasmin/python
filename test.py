def functionRead(filePointer):
    fileString = filePointer.read()
    print(fileString)

filePointer = open("textFile.txt", 'r')
functionRead(filePointer)
