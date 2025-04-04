def isPerfectSquare(num):
    # for i in range(1, num):
    #     if i * i == num:
    #         return True
    #     elif i * i > num:
    #         return False
    start = 1
    end = num
    while start <= end:
        mid = (start + end) // 2
        midsq = mid * mid
        print(midsq)
        if midsq == num:
            return True
        elif midsq < num:
            start = mid + 1
        else: 
            end = mid - 1
    return False

    
num = 100000000

print(isPerfectSquare(num))