def longestCommonPrefix(strs):
    for index in range(len(strs[0])):
        for string in strs:
            if string[index] != strs[0][index]:
                return string[:index]

test = ["force", "fortress", "focal", "cover"]

print(longestCommonPrefix(test))