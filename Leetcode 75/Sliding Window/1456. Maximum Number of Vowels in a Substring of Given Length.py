class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}
        def vowels_c(vow):
            count = 0
            for char in vow:
                if char in vowels:
                    count += 1
            return count

        substring = s[:k]
        initial_count = vowels_c(substring)
        maxV = max(0, initial_count)

        for i in range(len(s)-k):
            if substring[0] in vowels:
                initial_count -= 1
            if s[k+i] in vowels:
                initial_count += 1

            substring = substring[1:] + s[k+i]
            maxV = max(maxV, initial_count)
        return maxV

"""
- Here we are first identifying the no of vowels in the substring and then checking for no of substring count in each window by adding and substracting count depeding on whether vowels are added or not.
Time Complexity O(n)
Space COmplexity O(1)
"""
