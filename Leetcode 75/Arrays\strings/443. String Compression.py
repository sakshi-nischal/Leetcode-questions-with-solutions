# Approach 1: Using While loop
class Solution:
    def compress(self, chars) -> int:
        len_chars = len(chars)
        if not chars:
            return 0
        if len_chars == 0 or len_chars == 1:
            return len_chars
        
        idx = 0 # Index for the modification of the array
        i = 0 # Index for iteration of the array
        

        while i < len_chars:
            count = 0
            curr = chars[i]
            # Checking for duplicates
            while i < len_chars and chars[i] == curr:
                count += 1
                i += 1
            # Assigning the duplicates count as strings to the array
            chars[idx] = curr
            idx += 1
            # if ['a', 'b'] we need to return only ['a', 'b'] and not ['a', '1', 'b','2']
            if count > 1:
                # For handling the case when count becomes more than one digit number.
                # '12' as '1', '2'
                for digit in str(count):
                    chars[idx] = digit
                    idx += 1
        return idx

"""
Time complexity O(n)
Space Complexity O(1)
"""

# Approach 2: Using For loop
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # Handling string with length less than 1
        if len(chars) == 0 or len(chars) == 1:
            return len(chars)

        j = 0
        count = 1

        for i in range(len(chars) - 1):
            # If next element is same then update the count
            if chars[i] == chars[i + 1]:
                count += 1
            else:
                # If not same then store the currect element at j and update the counter
                chars[j] = str(chars[i])
                j += 1
                # Handle double digit count
                if count > 1:
                    for digit in str(count):
                        chars[j] = digit
                        j += 1
                count = 1
        # Handling last element
        chars[j] = str(chars[len(chars) - 1])
        j += 1
        if count > 1:
            for digit in str(count):
                chars[j] = digit
                j += 1

        return j

"""
Time complexity O(n)
Space Complexity O(1)
"""
