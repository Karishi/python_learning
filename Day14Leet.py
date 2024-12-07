def alphaOnly(string):
    alphanumeric = "abcdefghijklmnopqrstuvwxyz1234567890"
    output = ""
    for char in string:
        if char in alphanumeric:
            output += char
    print(output)
    return output

def isPalindrome(testString: str):
    testString = testString.lower()
    print(testString)
    output = alphaOnly(testString)
    for char in range(len(output)//2):
        if output[char] != output[-1 * (char+1)]:
            print(output + " isn't a palindrome.")
    print(output + " is a palindrome.")
    return True

test = "A man, a plan, a canal, Panama"

isPalindrome(test)