def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    deleted = 0
    for i in range(1, len(nums)):
        i -= deleted
        if nums[i] == nums[i-1]:
            del nums[i]
            deleted += 1
    return len(nums)

testList = [1, 1, 1, 2, 2, 3, 3, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7]
numUniques = removeDuplicates(testList)
print(f"There are {numUniques} unique values in the Test List.")
print(testList)