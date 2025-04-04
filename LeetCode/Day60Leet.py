def canJump(nums):
    def recurse(distance = nums[0], index = 0, success = False):
        if distance == 0 or success:
            return success
        distance = nums[index]
        print(f"distance {distance} | index {index} | goal {len(nums)}")
        

        if distance + index >= len(nums):
            return True
        success = recurse(distance, index + distance, success)
        if not success and distance > 0:
            success = recurse(distance - 1, index + distance, success)
        return success
    return recurse()

test = [2,3,1,3,0,0,4]

print(canJump(test))