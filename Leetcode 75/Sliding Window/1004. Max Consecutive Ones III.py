class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        max_count = 0

        for right, num in enumerate(nums):
            k -= 1-num

            if  k<0:
                k += 1-nums[left]
                left += 1
            else:
                max_count = max(max_count, right-left+1)
        return max_count


        # [1,1,1,0,0,0,1,1,1,1,0]
        # left = 0,0,0,0,0,1
        # right = 0,1,2,3,4,5,6
        # max_count = 0->1,2,3,4,5,5,6
        # num = 1,1,1,0,0,0,1
        # k = 2,2,2,1,0,-1,0
        #               k = -1+1 = 0
