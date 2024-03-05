class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        strg = ""
        min_len = min(len(word1), len(word2))
        for i, j in zip(word1, word2):
            strg = strg+ (i+j)
        if len(word1) > len(word2):
            strg = strg + word1[min_len:]
        else:
            strg = strg + word2[min_len:]
        
        return strg

'''
Time  Complexity: O(n)
Space Complexity: O(n)
'''
