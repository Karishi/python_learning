def balancedSum(arr):
    # Write your code here
    if len(arr) == 0 or sum(arr) == 0:
        return 0
    for index in range(1, len(arr)):
        if sum(arr[0:index]) == sum(arr[index+1:len(arr)]):
            return index

test = [0,0,0,0]

print(balancedSum(test))