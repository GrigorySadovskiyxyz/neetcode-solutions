from collections import Counter

class Solution(object):
    def containsDuplicate(self, nums):
        obj_of_nums = Counter(nums)
        a = None
        for each in obj_of_nums:
            if obj_of_nums[each] >= 2:
                a = True
                break
            else:
                a = False  
        return a
