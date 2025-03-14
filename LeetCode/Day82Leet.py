def singleNumber(nums):
    dupes = []
    unique = []
    for i in range(len(nums)):
        if nums[i] in nums[i+1:] and nums[i] not in dupes:
            dupes.append(nums[i])
        if nums[i] not in dupes:
            unique.append(nums[i])
    return unique

test = [1,2,1,3,2,5]

print(singleNumber(test))