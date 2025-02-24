def isHappy(n):
    checked = []
    val = n
    while val not in checked and val != 1:
        checked.append(val)
        total = 0
        for digit in str(val):
            total += int(digit) * int(digit)
        print(total)
        val = total
    if val in checked:
        return False
    if val == 1:
        return True
    
test = 2

print(isHappy(test))