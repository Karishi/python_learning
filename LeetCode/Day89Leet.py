def maxProduct(words):
    best = 0
    L = 0
    R = 1
    while L < len(words) - 2:
        for letter in words[L]:
            success = True
            if letter in words[R]:
                success = False
                break
        if success and best < len(words[L]) * len(words[R]):
            best = len(words[L]) * len(words[R])
        if R < len(words) - 1:
            R += 1
        else:
            L += 1
            R = L + 1
    
    return best

words = ["abcw","baz","foo","bar","xtfn","abcdef"]

print(maxProduct(words))