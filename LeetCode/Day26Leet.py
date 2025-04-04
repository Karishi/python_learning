# Make a function that justifies a string on a series of lines of text.

def justify(words, lineWidth):
    lines = []
    line = []
    currentLineSize = 0

    while len(words) > 0:
        word = words.pop(0)
        if currentLineSize > 0:
            currentLineSize += 1
        if currentLineSize + len(word) == lineWidth:
            line.append(word)
            lines.append(line)
            currentLineSize = 0
            line = []
        elif currentLineSize + len(word) > lineWidth:
            lines.append(line)
            currentLineSize = len(word)
            line = [word]
            if len(words) == 0:
                lines.append(line)
        else:
            line.append(word)
            currentLineSize += len(word)
            if len(words) == 0:
                lines.append(line)
    
    stringLines = []
    for line in lines:
        sumChar = 0
        string = ""
        for word in line:
            sumChar += len(word)
        numSpaces = lineWidth - sumChar
        numOpenings = len(line) - 1
        if numOpenings > 0:
            spaces = []
            for i in range(numOpenings):
                spaces.append("")
            i = 0
            while i < numSpaces:
                i += 1
                spaces[(i % numOpenings)-1] += " "
        string += line[0]
        for i in range(len(line)-1):
            string += spaces[i]
            string += line[i+1]
        stringLines.append(string)
                


    return stringLines

        

words = ["I", "know", "what", "you", "really", "really", "want,", "so", "don't", "try", "to", "dispute", "it."]

for line in justify(words, 17):
    print(line)