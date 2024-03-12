class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero, non_zero = 0, 0
        while non_zero < len(nums):
            if nums[non_zero] != 0:
                nums[zero], nums[non_zero] = nums[non_zero], nums[zero]
                non_zero += 1
                zero += 1
            else: 
                non_zero += 1
        return nums

"""
Time Complexity O(n)
Space Complexity O(1)
"""
