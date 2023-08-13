class Solution(object):
    def twoSum(self, nums, target):
        for index1, one in enumerate(nums):
            for i in range(index1 + 1, len(nums)):
                if one + nums[i] == target:
                    return [index1, i]

