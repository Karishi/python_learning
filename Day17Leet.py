def lengthOfLongestSubstring(string: str):
    longest = ""
    
    for startLetter in range(len(string)):
        current = ""
        i = startLetter
        while string[i] not in current and i < len(string)-1:
            current += string[i]
            i += 1
        if len(current) > len(longest):
            longest = current
    return f"The longest substring is {len(longest)} characters: {longest}"

test = "Sphinx of black quartz, judge my vow!"

print(lengthOfLongestSubstring(test))