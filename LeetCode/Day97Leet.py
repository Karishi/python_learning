def longestPalindrome(s):
    my_dict = {}
    for char in s:
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1
    odd_present = False
    total = 0
    for key in my_dict:
        if my_dict[key] % 2 == 0:
            total += my_dict[key]
        else:
            odd_present = True
            total += my_dict[key] -1
    if odd_present:
        total += 1
    return total

s = "ccabccccdd"
print(longestPalindrome(s))