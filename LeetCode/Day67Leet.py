def isHappy(n):
    checked = []
    while n not in checked and n != 1:
        checked.append(n)
        total = 0
        for digit in str(n):
            total += int(digit) * int(digit)
        print(total)
        n = total
    if n in checked:
        return False
    if n == 1:
        return True
    
test = 2

print(isHappy(test))