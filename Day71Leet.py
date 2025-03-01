def convertToTitle(columnNumber):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    output = ""
    while (columnNumber - 1) // 26 > 0:
        output += alphabet[columnNumber % 26 - 1]
        columnNumber = columnNumber // 26
    output += alphabet[columnNumber % 26 - 1]

    return output[::-1]

test = 23
print(convertToTitle(test))