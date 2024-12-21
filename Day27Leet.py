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


def longestPalindrome(s: str):
    substring = s
    belowMax = 0
    while True:
        left = 0
        right = len(s)-belowMax
        for i in range(belowMax+1):
            if(isPalindrome(substring)):
                return substring
            left += i
            right += i
            substring = s[left:right]

        belowMax += 1


test = "ablewasIereIsawelbow"

print(longestPalindrome(test))