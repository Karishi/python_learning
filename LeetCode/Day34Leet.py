def minWindow(s, t):
    def t_in_s(s, t = t):
        tvalues = {}
        for char in t:
            if char in tvalues:
                tvalues[char] += 1
            else:
                tvalues[char] = 1

        starterString = ""
        tValuesTestCopy = tvalues
        for char in range(len(s)):
            if s[char] in tValuesTestCopy:
                tValuesTestCopy[s[char]] -= 1
                starterString += s[char]
                if tValuesTestCopy[s[char]] == 0:
                    del tValuesTestCopy[s[char]]
                    if len(tValuesTestCopy) == 0:
                        return True
        return False
    
    lIndex = 0
    rIndex = len(t)
    best = ""
    if t_in_s(s, t):
        best = s
    else:
        return best
    
    while rIndex <= len(s):
        substring = s[lIndex:rIndex]
        if t_in_s(substring):
            if len(substring) < len(best):
                best = substring
            lIndex += 1
        else:
            rIndex += 1
    return best
            
        

    
    
                
    

    
test = "ADOBECODEBANC"
test2 = "ABC"

print(minWindow(test, test2))