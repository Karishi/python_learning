def isMatch(s, p):
    if "*" in p:
        return True
    
    if len(p) != len(s):
        return False

    for i in range(len(s)):
        if p[i] != "?" and s[i] != p[i]:
            return False
    return True

t1 = "abracadabra"
t2 = "?bracada?br"

print(isMatch(t1, t2))