def convert(string, numRows):
    zigZagArray = [ [None]*((len(string)//(numRows//2))) for i in range(numRows)]
    zigging = True
    xIndex = 0
    yIndex = 0
    stringIndex = 0
    zigZagArray[yIndex][xIndex] = string[stringIndex]
    stringIndex += 1
    while stringIndex < len(string):
        stringIndex += 1
        if zigging:
            yIndex += 1
            if yIndex == numRows - 1:
                zigging = False
        else:
            yIndex -= 1
            xIndex += 1
            if yIndex == 0:
                zigging = True
        zigZagArray[yIndex][xIndex] = string[stringIndex-1]
    myString = ""
    for row in zigZagArray:
        for letter in row:
            if letter:
                myString += letter
    print(myString)
    return zigZagArray

s = "paypalishiring"
testNum = 5

for row in convert(s, testNum):
    print(row)