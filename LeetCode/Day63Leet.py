def reverseWords(s):
    flipped_word_list = []
    
    s = s.strip()

    word = ""
    for char in s:
        if char != " ":
            word += char
        else:
            flipped_word_list.insert(0, word)
            word = ""
    flipped_word_list.insert(0, word)

    flipped_s = ""
    for word in flipped_word_list:
        flipped_s += word + " "
    flipped_s = flipped_s.strip()
    
    return flipped_s

test = "the sky is blue"

print(reverseWords(test))