# PROBLEM NUMBER: 257
# https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/
# 257.Minimum Length of String After Deleting Similar Ends
# DIFFICULTY: EASY
class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Approach:
        # We need to repeatedly remove matching characters from both the beginning
        # and the end of the string as long as they are the same.
        
        # Step 1: Initialize two pointers:
        #         left  → start of the string
        #         right → end of the string
        
        # Step 2: While left < right and the characters at both ends are equal:
        #         • Let c be the character at the current ends.
        
        # Step 3: Move the left pointer forward while s[left] == c,
        #         skipping all consecutive occurrences of c from the left side.
        
        # Step 4: Move the right pointer backward while s[right] == c,
        #         skipping all consecutive occurrences of c from the right side.
        
        # Step 5: Continue this process until the characters at the ends differ
        #         or the pointers cross.
        
        # Step 6: The remaining substring length is:
        #         right - left + 1
        
        # Step 7: Return this length.

     
        left = 0
        right = len(s) - 1

        while left < right and s[left] == s[right]:
            c = s[left]

            while left <= right and s[left] == c:
                left += 1

            while left <= right and s[right] == c:
                right -= 1

        return right - left + 1