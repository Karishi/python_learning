def reverseBits(n):
    x = 1
    total = 0
    for char in str(n):
        if char == "1":
            total += x
        x *= 2
    return total

n = "11111111111111111111111111111101"
print(reverseBits(n))