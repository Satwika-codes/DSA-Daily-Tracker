# PROBLEM NUMBER: 1876
# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/
# 1876.Substrings of Size Three with Distinct Characters
# DIFFICULTY: EASY
class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Approach:
        # We need to count substrings of length 3 where all characters are distinct.
        #
        # Step 1: Iterate through the string from index 0 to len(s) - 3.
        #         This ensures we can always take a substring of length 3.
        #
        # Step 2: For each index i, take substring s[i:i+3].
        #
        # Step 3: Convert this substring into a set.
        #         If all characters are unique, the set size will be 3.
        #
        # Step 4: If len(set(s[i:i+3])) == 3, increment count.
        #
        # Step 5: Return the final count.
      
        count = 0

        for i in range(len(s) - 2):
            if len(set(s[i:i+3])) == 3:
                count += 1

        return count
        