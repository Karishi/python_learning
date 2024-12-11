# Task: Find the median of two sorted lists.

def findMedianSortedArrays(nums1, nums2):
    num1index = 0
    num2index = 0
    numsCombined = []
    while num1index < len(nums1) and num2index < len(nums2):
        if nums1[num1index] < nums2[num2index]:
            numsCombined.append(nums1[num1index])
            num1index += 1
        else:
            numsCombined.append(nums2[num2index])
            num2index += 1
    while num1index < len(nums1):
        numsCombined.append(nums1[num1index])
        num1index += 1
    while num2index < len(nums2):
        numsCombined.append(nums2[num2index])
        num2index += 1
    if len(numsCombined) % 2 == 0:
        lower = numsCombined[len(numsCombined)//2 - 1]
        higher = numsCombined[(len(numsCombined)//2)]
        return (lower + higher) / 2
    else:
        return numsCombined[len(numsCombined)//2]

test = [1,2,5]
test2 = [3, 4, 7]

print(findMedianSortedArrays(test, test2))