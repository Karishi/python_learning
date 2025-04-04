def myAtoi(s):
    numbers = "0123456789"
    new = ""
    s = s.strip()
    index = 0
    if s[0] == "-":
        new += s[index]
        index += 1
    while index < len(s) and s[index] in numbers:
        new += s[index]
        index += 1
    if len(new) == 0 or new == "-":
        new = 0
    return int(new)

test = "42"

print(myAtoi(test))