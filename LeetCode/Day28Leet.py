def climbStairs(height):
    early = 0
    previous = 1
    additive = 0
    for i in range(height):
        additive = previous + early
        early = previous
        previous = additive
    return previous

print(f"For 10 stairs, there are {climbStairs(10)} methods.")
            