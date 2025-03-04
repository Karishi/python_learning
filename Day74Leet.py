def groupAnagrams(strs):
    grouped_strings = []
    for string in strs:
        count = 0
        group_found = False
        for group in grouped_strings:
            match = True
            for item in group:
                for letter in item:
                    if letter not in string:
                        match = False
                        break
                if match == False:
                    break
            if match:
                group.append(string)
                group_found = True
        if not group_found:
            grouped_strings.append([string])
    return grouped_strings

test = ["eat","tea","tan","ate","nat","bat"]

print(groupAnagrams(test))