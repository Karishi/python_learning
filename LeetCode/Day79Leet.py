def isIsomorphic(s, t):
    used = {}
    for i in range(len(s)):
        if s[i] in used and used[s[i]] != t[i]:
            return False
        else:
            used[s[i]] = t[i]
    used = {}
    for i in range(len(t)):
        if t[i] in used and used[t[i]] != s[i]:
            return False
        else:
            used[t[i]] = s[i]
    return True

s = "tumblr"
t = "eagles"

print(isIsomorphic(s, t))