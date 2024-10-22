def printFileInUpperCase(fileName):
    # Opens the text file
    fhand = open(fileName)
    # .read() turns contents of the file to a string
    inp = fhand.read()
    print(inp.upper())

printFileInUpperCase(fileName="mbox-short.txt")