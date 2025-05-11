def insertion_sort(nums):
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            swap = nums[j]
            nums[j] = nums[j-1]
            nums[j-1] = swap
            j -= 1
    return nums