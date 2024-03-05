# Approach 1: Using For Loop
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = second = float('inf')
        for no in nums:
            if no <= first:
                first = no
            elif no <= second:
                second = no
            else:
                return True
        return False
"""
Time Complexity O(n)
Space Complexity O(1)
"""

# Approach 2: Using While Loop
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = float("inf")
        sec = float("inf")
        i=0
        while i<len(nums):
            if nums[i]<=first:
                first = nums[i]
            elif nums[i]<=sec:
                sec = nums[i]
            else:
                return True
            i += 1
        return False
"""
Time Complexity O(n)
Space Complexity O(1)
"""
            
        
