# PRBLEM NUMBER: 2825
# https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/
# 2825. Make String a Subsequence Using Cyclic Increments
# DIFFICULTY: HARD
class Solution(object):
    def canMakeSubsequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        # Approach:
        # We need to check if str2 can be formed as a subsequence of str1.
        # Allowed operation: each character in str1 can either:
        #   1) stay the same
        #   2) be incremented cyclically by 1 (z → a)
        
        # Idea:
        # Use two pointers:
        #   i → traverse str1
        #   j → traverse str2
        
        # Step 1: Compare characters from str1 and str2.
        # Step 2: For each character c1 in str1:
        #         - Compute its cyclic increment:
        #           next_c1 = next character in alphabet (z wraps to a)
        # Step 3: If either:
        #         • c1 == c2
        #         • next_c1 == c2
        #         then we can match this character of str2.
        # Step 4: Move pointer j when a match occurs.
        # Step 5: Always move pointer i.
        # Step 6: If we matched all characters of str2 → return True.

        i = 0  # pointer for str1
        j = 0  # pointer for str2

        while i < len(str1) and j < len(str2):
            c1 = str1[i]
            c2 = str2[j]

            # compute cyclic increment of c1
            next_c1 = chr((ord(c1) - ord('a') + 1) % 26 + ord('a'))

            if c1 == c2 or next_c1 == c2:
                j += 1

            i += 1

        return j == len(str2)