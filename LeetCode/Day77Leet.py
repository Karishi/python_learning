def trailingZeroes(n):
    # x = n
    # total = 1
    # while x > 1:
    #     total *= x
    #     x -= 1
    # y = int(total)
    # count = 0
    # while y % 10 == 0:
    #     y = y // 10
        # count += 1
    
    return n//5 + n//(5**2) + n//(5**3) + n//(5**4) + n//(5**5)

print(trailingZeroes(25))