# PROBLEM NUMBER: 942
# https://leetcode.com/problems/di-string-match/
# 942. DI String Match
# DIFFICULTY: EASY
class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        # Approach:
        # We are given a string s consisting of characters 'I' (increase) and 'D' (decrease).
        # We need to construct a permutation of numbers from 0 to n (where n = len(s))
        # such that the relationship between consecutive numbers follows the pattern.
        
        # Step 1: Initialize two pointers:
        #         low  → smallest available number (0)
        #         high → largest available number (n)
        
        # Step 2: Create an empty list "result" to store the permutation.
        
        # Step 3: Traverse each character in the string s.
        
        # Step 4: If the character is 'I':
        #         • Append the current smallest number (low) to result.
        #         • Increment low because that number is now used.
        
        # Step 5: If the character is 'D':
        #         • Append the current largest number (high) to result.
        #         • Decrement high because that number is now used.
        
        # Step 6: After processing all characters, only one number remains
        #         (low == high). Append this last number to the result.
        
        # Step 7: Return the constructed permutation.

        low = 0
        high = len(s)
        result = []

        for c in s:
            if c == 'I':
                result.append(low)
                low += 1
            else:
                result.append(high)
                high -= 1

        result.append(low)

        return result
        