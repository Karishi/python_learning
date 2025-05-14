def count_word(terms, target):
    words = {}
    for word in terms:
        if word.lower() in words:
            words[word.lower()] += 1
        else:
            words[word.lower()] = 1
    if target in words:
        return words[target]
    else:
        return 0