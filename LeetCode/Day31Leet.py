def convert(string, numRows):
    zigZagArray = [[] for i in range(numRows)]
    zigging = True
    yIndex = 0
    stringIndex = 0
    zigZagArray[yIndex].append(string[stringIndex])
    stringIndex += 1
    while stringIndex < len(string):
        if zigging:
            yIndex += 1
            if yIndex == numRows - 1:
                zigging = False
        else:
            yIndex -= 1
            if yIndex == 0:
                zigging = True
        zigZagArray[yIndex].append(string[stringIndex])
        stringIndex += 1

    myString = ""
    for row in zigZagArray:
        for letter in row:
            if letter:
                myString += letter
    return myString


s = "paypalishiring"
testNum = 3

print(f"The encoded term {s} turns into {convert(s, testNum)} when using {testNum} rows.")