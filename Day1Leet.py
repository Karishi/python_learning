
def twoSum(nums: list[int], target: int):
    for val1 in range(0, len(nums)):
        # Having value 2 start from the space after value 1 as it iterates, we avoid ever having repeated combinations.
        # This keeps us from getting into O(n^2) territory.
        val_2_start = val1 + 1
        for val2 in range(val_2_start, len(nums)):
            if nums[val1] + nums[val2] == target:
                output = f"[{val1}, {val2}]"
                explanation = f"Because nums[{val1}] + nums[{val2}] == {target}, we return [{val1}, {val2}]"
                return output, explanation
            
print("Input: nums = [2, 7, 11, 15], target = 26")
nums = [2, 7, 11, 15]
target = 26
output, explanation = twoSum(nums, target)
print("Output: " + output)
print("Explanation: " + explanation)