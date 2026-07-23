class Solution(object):

    nums = [3, 2, 4]
    target = 6

    def twoSum(self, nums, target):
        ''' 
        :type nums: List[int]
        :type target: int
        :rtype: List[int]'''
        seen = {}
        for index, num in enumerate(nums):
            second_value = target - num
            if second_value in seen:
                return [seen[second_value], index]
            seen[num] = index