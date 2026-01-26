# PROBLEM NUMBER: 917
# https://leetcode.com/problems/reverse-only-letters/
# Reverse Only Letters
# DIFFICULTY: MEDIUM
class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """        
        # Approach:
        # - Use two pointers: left starting at 0, right starting at len(s)-1.
        # - Swap letters at left and right while skipping non-letter characters.
        # - Move left forward and right backward only when letters are swapped.
        # - Non-letter characters remain in their original positions.
        # - Build the final string by converting the list of characters back to a string.

        # Time Complexity: O(n)
        # Space Complexity: O(n) due to conversion to list
        

        s = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            if not s[left].isalpha():
                left += 1
                continue
            if not s[right].isalpha():
                right -= 1
                continue
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return ''.join(s)
