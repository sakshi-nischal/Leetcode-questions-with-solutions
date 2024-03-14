class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        max_altitude = 0
        curr_altitude = 0
        for i in range(len(gain)):
            curr_altitude += gain[i]
            if max_altitude < curr_altitude:
                max_altitude = curr_altitude
        return max_altitude

'''
Time Complexity: O(n)
Space Complexity: O(1)
'''
