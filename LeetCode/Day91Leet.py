def isPerfectSquare(num):
    for i in range(1, num):
        if i * i == num:
            return True
        elif i * i > num:
            return False
    
num = 20449

print(isPerfectSquare(num))