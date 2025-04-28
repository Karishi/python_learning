def addAll(X, total = 0):
    if X == 0:
        return total
    total += addAll(X-1, total)
    return total + X

print(addAll(5))