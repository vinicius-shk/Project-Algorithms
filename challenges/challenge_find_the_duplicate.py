def find_duplicate(nums: list = [1]):
    nums.sort()
    for index, num in enumerate(nums[1::]):
        if num == nums[index] and num > 0:
            return num
    return False
