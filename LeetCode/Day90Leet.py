def countNumbersWithUniqueDigits(n):
    if n == 0:
        return 1
    oneVal = 10
    if n == 1:
        return oneVal

    base = 9
    mult = 9
    for i in range(1, n):
        base *= mult
        mult -= 1
    return base + oneVal

test = 2

print(countNumbersWithUniqueDigits(test))