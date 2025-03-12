def addDigits(num):
    while len(str(num)) > 1:
        total = 0
        for i in str(num):
            total += int(i)
        num = total
        print(num)
    return num

test = 21
print(addDigits(test))