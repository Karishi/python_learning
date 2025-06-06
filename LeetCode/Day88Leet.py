def countSmaller(nums):
    # for i in range(len(nums)):
    #     count = 0
    #     for j in range(i+1, len(nums)):
    #         if nums[i] > nums[j]:
    #             count += 1
    #     nums[i] = count
    # return nums
    def sort(enum):
        half = len(enum) / 2
        if half:
            left, right = sort(enum[:half]), sort(enum[half:])
            m, n = len(left), len(right)
            i = j = 0
            while i < m or j < n:
                if j == n or i < m and left[i][1] <= right[j][1]:
                    enum[i+j] = left[i]
                    smaller[left[i][0]] += j
                    i += 1
                else:
                    enum[i+j] = right[j]
                    j += 1
        return enum
    smaller = [0] * len(nums)
    sort(list(enumerate(nums)))
    return smaller
    



nums = [5,2,6,1]

print(countSmaller(nums))