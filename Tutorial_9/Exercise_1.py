def printFileInUpperCase(fileName):
    fhand = open(fileName)
    inp = fhand.read()
    print(inp.upper())

printFileInUpperCase(fileName="mbox-short.txt")