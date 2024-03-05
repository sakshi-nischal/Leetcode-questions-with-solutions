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
