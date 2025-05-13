def selection_sort(nums):
    for index in range(len(nums)):
        smallest = index
        for idx in range(smallest+1, len(nums)):
            if nums[smallest] > nums[idx]:
                smallest = idx
        nums[index], nums[smallest] = nums[smallest], nums[index]
    return  nums