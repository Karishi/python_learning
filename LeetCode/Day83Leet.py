def nthUglyNumber(n):
    def isUgly(num):
        while num != 1:
            if num % 2 != 0 and num % 5 != 0 and num % 3 != 0:
                return False
            if num % 2 == 0:
                num = num // 2
            if num % 3 == 0:
                num = num // 3
            if num % 5 == 0:
                num = num // 5
        return True
    
    numUglies = 0
    i = 0
    while numUglies < n:
        i += 1
        if isUgly(i):
            numUglies += 1
    return i

test = 9

print(nthUglyNumber(test))