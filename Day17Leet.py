def lengthOfLongestSubstring(string: str):
    longest = ""
    
    for startLetter in range(len(string)):
        current = ""
        i = startLetter
        while string[i] not in current and i < len(string)-1 and startLetter < len(string) - len(longest):
            current += string[i]
            i += 1
        if len(current) > len(longest):
            longest = current
    return f"The longest substring is {len(longest)} characters: {longest}"

test = "abcabcad"

print(lengthOfLongestSubstring(test))