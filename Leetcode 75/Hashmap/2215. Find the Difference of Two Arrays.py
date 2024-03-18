class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """

        answer = []
        num_map1 = {}
        ans1 = []
        num_map2 = {}
        ans2 = []
        for i in nums1:
            num_map1[i] = num_map1.get(i,0)+1
        for i in nums2:
            num_map2[i] = num_map1.get(i,0)+1
        for i in set(num_map1.keys()):
            if i not in set(num_map2.keys()):
                ans1.append(i)
        answer.append(ans1)
        for i in set(num_map2.keys()):
            if i not in set(num_map1.keys()):
                ans2.append(i)
        answer.append(ans2)
        return answer
        
