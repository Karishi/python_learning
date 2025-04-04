def mySqrt(x):
    attempt = 1
    while x/attempt > attempt:
        attempt += 1
    if attempt > x/attempt:
        return attempt-1
    else:
        return attempt

test = 99

print(mySqrt(test))