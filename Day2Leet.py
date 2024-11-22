# Assignment: Given two binary strings, add them together and return the value as a binary string.

def sumBinary(a: str, b: str):
    output = bin(int(a, 2) + int(b, 2))
    return output[2:]

print("Input: a = 1010, b = 1011")
a = "1010"
b = "1011"
output = sumBinary(a, b)
print("Output: " + output)