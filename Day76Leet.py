def combinationSum3(k, n):
    successes = []
    attempt = []
    def recurse(count = 0, value = 1):
        if count > k or sum(attempt) > n:
            attempt.pop()
            return
        
        attempt.append(value)

        if count == k and sum(attempt) == n:
            success = []
            for item in attempt:
                success.append(item)
            successes.append(success)
        elif value < 10:
            recurse(count, value + 1)
            recurse(count + 1, value + 1)
    recurse()
    return successes
        
values = 3
target = 9

print(combinationSum3(values, target))