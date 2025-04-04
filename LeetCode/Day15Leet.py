def alphaOnly(string):
    alphanumeric = "abcdefghijklmnopqrstuvwxyz1234567890"
    output = ""
    for char in string:
        if char in alphanumeric:
            output += char
    return output

def isPalindrome(testString: str):
    testString = testString.lower()
    output = alphaOnly(testString)
    for char in range(len(output)//2):
        if output[char] != output[-1 * (char+1)]:
            return False
    return True

def combinatoric_palindrome_hunt(s: str):
    if not s:
        yield []
        return

    for i in range(1, len(s) + 1):
        for part in combinatoric_palindrome_hunt(s[i:]):
            if isPalindrome(str([s[:i]])):
                yield [s[:i]] + part
            
def partition(s: str):
    output = []
    for part in combinatoric_palindrome_hunt(s):
        partOfOutput = True
        i = 0
        while partOfOutput is True and i < len(part):
            if not isPalindrome(part[i]):
                partOfOutput = False
            i += 1
        if partOfOutput:
            output.append(part)
    return output

test = "racecar"

for part in combinatoric_palindrome_hunt(test):
    print(part)