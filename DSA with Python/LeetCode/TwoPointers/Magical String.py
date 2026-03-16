# PROBLEM NUMBER: 481
# https://leetcode.com/problems/magical-string/
# 481. Magical String
# DIFFICULTY: MEDIUM
class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Approach:
        # The magical string is a sequence consisting only of 1's and 2's such that
        # the counts of consecutive numbers form the string itself.
        
        # Example magical string:
        # 1 2 2 1 1 2 1 2 2 1 2 2 ...
        # Grouped counts:
        # 1 | 22 | 11 | 2 | 1 | 22 ...
        # Counts → 1 2 2 1 1 2 ...
        
        # Step 1: Handle small edge cases.
        #         If n <= 0 return 0.
        #         If n <= 3 return 1 because the first three digits are [1,2,2]
        #         which contain only one '1'.
        
        # Step 2: Initialize the magical string with the known starting pattern:
        #         s = [1, 2, 2]
        
        # Step 3: Use pointer i to read how many times the next number should appear.
        
        # Step 4: Maintain a variable "num" that represents the next number to append
        #         (alternates between 1 and 2).
        
        # Step 5: While the length of the string is less than n:
        #         • Read s[i] which tells how many times to append num.
        #         • Extend the list with that many copies of num.
        #         • Toggle num between 1 and 2 using: num = 3 - num
        #         • Move pointer i forward.
        
        # Step 6: After generating enough elements, take the first n elements
        #         and count how many 1's are present.
        if n <= 0:
            return 0
        if n <= 3:
            return 1

        s = [1, 2, 2]
        i = 2
        num = 1

        while len(s) < n:
            s.extend([num] * s[i])
            num = 3 - num  # switch between 1 and 2
            i += 1

        return s[:n].count(1)