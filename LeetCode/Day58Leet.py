def myPow(x, n):
    flip = False
    if n == 0:
        return 1
    
    if n == 1:
        return x

    if n < 0:
        num = -1 * n
        flip = True
    else:
        num = n

    xc = x
    for i in range(1, num):
        xc *= x
    
    if flip:
        xc = 1 / xc
    return xc

testx = 2
testn = -2

print(myPow(testx, testn))