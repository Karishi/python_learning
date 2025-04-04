def lastWord(string):
    s = string.strip()
    char = s[-1]
    count = 0
    
    while char != " ":
        count += 1
        char = s[-1 * count]
    
    return count - 1

test = "  Hello World   "

print(f"The number of letters in the last word of the string is {lastWord(test)}")