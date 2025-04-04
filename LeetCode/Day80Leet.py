def addDigits(num):
    while len(str(num)) > 1:
        print(num)
        total = 0
        for i in str(num):
            total += int(i)
        num = total
    return num

test = 21
print(addDigits(test))