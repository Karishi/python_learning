def isIsomorphic(s, t):
    used = {}
    for i in range(len(s)):
        if s[i] in used and used[s[i]] != t[i]:
            return False
        else:
            used[s[i]] = t[i]
    return True

s = "foo"
t = "bar"

print(isIsomorphic(s, t))