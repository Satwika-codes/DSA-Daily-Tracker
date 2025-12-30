# PROBLEM NUMBER:1189
# https://leetcode.com/problems/maximum-number-of-balloons
# 1189.Maximum Number of Balloons
# DIFFICULTY:HARD
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        APPROACH:
        - Count the frequency of each character in the input string.
        - The word "balloon" requires:
              b → 1, a → 1, l → 2, o → 2, n → 1
        - Determine how many times each required character can be formed.
        - The minimum of these values gives the maximum number of "balloon"
          instances that can be formed.
        """

        from collections import Counter

        freq = Counter(text)

        return min(
            freq.get('b', 0),
            freq.get('a', 0),
            freq.get('l', 0) // 2,
            freq.get('o', 0) // 2,
            freq.get('n', 0)
        )
