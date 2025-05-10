def merge_sort(nums):
    if len(nums) < 2:
        return nums
    left = nums[:len(nums)//2]
    right = nums[len(nums)//2:]
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    return merge(sorted_left, sorted_right)


def merge(first, second):
    final = []
    i = 0
    j = 0
    for total in range(len(first)+len(second)):
        if i == len(first):
            final.append(second[j])
            j += 1
        elif j == len(second):
            final.append(first[i])
            i += 1
        elif first[i] < second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1
    return final