# PROBLEM NUMBER:1370
# https://leetcode.com/problems/increasing-decreasing-string/
# 1370.Incresing Decreasing String
# DIFFICULTY:EASY
class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """   
        # APPROACH:
        # - Count the frequency of each character in the string.
        # - Repeatedly append characters in increasing alphabetical order
        #   using available frequencies.
        # - Then append characters in decreasing alphabetical order.
        # - Continue this alternating process until all characters are used.

        from collections import Counter

        freq = Counter(s)
        result = []

        while len(result) < len(s):
            for c in sorted(freq):
                if freq[c] > 0:
                    result.append(c)
                    freq[c] -= 1

            for c in sorted(freq, reverse=True):
                if freq[c] > 0:
                    result.append(c)
                    freq[c] -= 1

        return "".join(result)
