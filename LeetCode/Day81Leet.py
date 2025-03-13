def isUgly(n):
    while n != 1:
        if n % 2 != 0 and n % 5 != 0 and n % 3 != 0:
            print(n)
            return False
        if n % 2 == 0:
            n = n // 2
        if n % 3 == 0:
            n = n // 3
        if n % 5 == 0:
            n = n // 5
    return True

test = 34

print(isUgly(test))