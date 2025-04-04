import math

def combinationSum3(k, n):
    successes = []
    attempt = []
    
    for i in range(k):
        attempt.append(i+1)
    
    count = 0
    while count < 10**k - 1:
        count += 1
        divvy = count
        i = 0
        if divvy % 10 not in attempt:
            attempt[i] = divvy % 10
        i += 1
        while divvy >= 10:
            divvy = divvy // 10
            if divvy % 10 not in attempt:
                attempt[i] = divvy % 10
            i += 1
        if 0 not in attempt and sum(attempt) == n:
            success = []
            for item in attempt:
                success.append(item)
            success.sort()
            if success not in successes:
                successes.append(success)

    return successes
        
values = 3
target = 9

print(combinationSum3(values, target))