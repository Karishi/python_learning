def hasSpecialSubstring(s, k):
    chain = 1
    for i in range(len(s)):
        print(f"chain is {chain} at {i}")
        if i < len(s)-1 and s[i] == s[i+1]:
            chain += 1
        else:
            if chain == k:
                return True
            chain = 1
    if chain == k:
         return True
    return False

test = "aabaaaa"
k = 3

print(hasSpecialSubstring(test, k))