class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        num_map= {}
        for i in arr:
            num_map[i] = num_map.get(i,0)+1
        if len(num_map.values()) == len(set(num_map.values())):
            return True
        return False
        
