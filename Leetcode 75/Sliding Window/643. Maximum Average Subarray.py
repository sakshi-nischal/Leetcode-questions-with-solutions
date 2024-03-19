class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        max_average = -float("inf")
        sum_num = float(sum(nums[0:k]))
        avg = float(sum_num)/k
        max_average = max(max_average,avg)

        for i in range(0,len(nums)-k):
            sum_num = sum_num-nums[i]+nums[i+k]
            avg = float(sum_num)/k
            max_average = max(max_average,avg)
            
        return max_average
