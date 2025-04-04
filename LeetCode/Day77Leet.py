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
    total = 0
    x = 5
    count = 0
    while n >= x:
        x *= 5
        count += 1

    while count > 0:
        total += n//(5**count)
        count -= 1

    return total

print(trailingZeroes(10))