class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_length = 0
        left = 0
        k = 1

        for right, num in enumerate(nums):
            k -= 1-num
            if k < 0:
                k += 1-nums[left]
                left += 1
            else:
                max_length = max(max_length, right-left)
        return max_length
        
