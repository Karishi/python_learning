# A few notes on making this easier for myself.
# Alphabet includes a blank space at the beginning so the index of each number starts at 1 naturally.
# I reverse the column title string so that we're working from small numbers to big numbers.

def titleToNumber(columnTitle):
    alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    flip = columnTitle[::-1]
    total = 0
    multiplier = 1
    for i in range(len(columnTitle)):
        total += multiplier * alphabet.index(flip[i])
        multiplier *= 26
    return total

test = "ZY"

print(titleToNumber(test))