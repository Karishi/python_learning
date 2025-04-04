def majorityElement(nums):
    elements = {}
    for item in nums:
        if item in elements:
            elements[item] += 1
            print(f"{item} count: {elements[item]}")
            if elements[item] >= len(nums)/2:
                return item
        else:
            elements[item] = 1
            print(f"Added {item} to dict")

test = [2,2,2,3,3]

print(majorityElement(test))