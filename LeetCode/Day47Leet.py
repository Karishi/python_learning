def generateParenthesis(n):
    parenList = []

    def recursiveParen(numL = 0, numR = 0, string = "", total = n):
        if numR > numL or numL > total:
            return
        
        if (numR + numL)/2 == total:
            parenList.append(string)

        recursiveParen(numL + 1, numR, string + "(")
        recursiveParen(numL, numR + 1, string + ")")
    
    recursiveParen()
    return parenList

test = 3

print(generateParenthesis(test))