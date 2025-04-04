def divide(dividend, divisor):
    count = 1
    negative = False
    if dividend < 0 and divisor >= 0:
        negative = True
        dividend *= -1
    elif divisor < 0 and dividend >= 0:
        negative = True
        divisor *= -1
    elif divisor < 0 and dividend < 0:
        divisor *= -1
        dividend *= -1

    while divisor * (count + 1) < dividend:
        count += 1
    
    modulo = dividend - divisor * (count)
    if negative:
        count *= -1
    return count, modulo

test = -25
val = 3

print(divide(test, val))