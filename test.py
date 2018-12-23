def functionRead(filePointer):
    fileString = filePointer.read()
    print(fileString )
    del fileString

filePointer = open("textFile.txt", 'r')
functionRead(filePointer)

