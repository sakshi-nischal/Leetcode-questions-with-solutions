# Two pointer appraoch
class Solution(object):
    def isSubsequence(self, s, t):``
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_p = 0 # s_p to track characters in string s
        t_p = 0 # t_p to track characters in string t.
        while s_p < len(s) and t_p < len(t):
            if s[s_p] == t[t_p]:
                s_p += 1
                t_p += 1
            else:
                t_p += 1
        return s_p == len(s)

"""
- Uses two pointers to keep track of the characters of the strings s and t.
- Then it tracks for the same character, and if the order fails, the value of s_p will not match the length of the subsequence string s if it is a subsequence.
Time Complexity O(n)
Space Complexity O(1)
"""
