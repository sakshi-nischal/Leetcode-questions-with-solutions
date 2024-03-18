class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        word_map1 = {}
        word_map2 = {}

        for i in word1:
            word_map1[i] = word_map1.get(i,0) + 1
        for i in word2:
            word_map2[i] = word_map2.get(i,0) + 1
        if sorted(word_map1.keys()) == sorted(word_map2.keys()) and sorted(word_map1.values()) == sorted(word_map2.values()):
            return True 
        

        
