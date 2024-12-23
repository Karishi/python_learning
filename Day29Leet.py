def plusOne(digits = []):
    x = len(digits) - 1
    is9 = True
    while x >= 0 and is9:
        if digits[x] == 9:
           digits[x] = 0
           x -= 1
        else:
            digits[x] += 1
            is9 = False
    if digits[0] == 0:
        digits.insert(0, 1)
    return digits

testList = [9, 9, 9]

print(plusOne(testList))