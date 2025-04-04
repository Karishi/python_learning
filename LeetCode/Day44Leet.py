def isPalindrome(x):
    s = str(x)

    for digit in range(len(s)//2):
        if s[digit] != s[-(digit+1)]:
            return False
    return True

test = "12345432"

print(f"Test number {test} is a palindrome: {isPalindrome(test)}")