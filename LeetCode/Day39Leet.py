def spiralIn(k):
    array = [ [0]*k for i in range(k) ]
    fail = 0
    x = 0
    y = 0
    count = 0
    right = True
    left = False
    up = False
    down = False
    
    def success(count, fail):
        count += 1
        array[y][x] = count
        fail = 0
        return count, fail

    while fail < 2:
        if right:
            if x < len(array)-1 and array[y][x+1] == 0:
                count, fail = success(count, fail)
                x += 1
            else:
                fail += 1
                right = False
                down = True
        elif down:
            if y < len(array)-1 and array[y+1][x] == 0:
                count, fail = success(count, fail)
                y += 1
                fail = 0
            else:
                fail += 1
                down = False
                left = True
        elif left:
            if x > 0 and array[y][x-1] == 0:
                count, fail = success(count, fail)
                x -= 1
                fail = 0
            else:
                fail += 1
                left = False
                up = True
        elif up:
            if y > 0 and array[y-1][x] == 0:
                count, fail = success(count, fail)
                y -= 1
                fail = 0
            else:
                fail += 1
                up = False
                right = True
    success(count, fail)
    return array
        


array = spiralIn(7)

for row in array:
    print(row)