# For a number n
# If you guess a number from 1 to n successfully, you win.
# Demonstrate binary search without an object-based tree.
def getMoneyAmount(n, guess):
    start = 1
    end = n
    mid = (start + end) // 2
    while start <= end-1:
        print(mid)
        if guess > mid:
            start = mid
            if end-start > 1:
                mid = (start + end) // 2
            else:
                mid += 1
        elif guess < mid:
            end = mid
            if end-start > 1:
                mid = (start + end) // 2
            else:
                mid -= 1
        elif guess == mid:
            return mid


test = 100
print(getMoneyAmount(test, 10))