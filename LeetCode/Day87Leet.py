def nthSuperUglyNumber(n, primes):
    def isUgly(num):
        while num != 1:
            shifted = False
            for j in range(len(primes)):
                if num % primes[j] == 0:
                    num = num // primes[j]
                    shifted = True
            if not shifted:
                return False
        return True

    numUglies = 0
    i = 0
    while numUglies < n:
        i += 1
        if isUgly(i):
            numUglies += 1
    return i

n = 12
primes = [2,7,13,19]

print(nthSuperUglyNumber(n, primes))