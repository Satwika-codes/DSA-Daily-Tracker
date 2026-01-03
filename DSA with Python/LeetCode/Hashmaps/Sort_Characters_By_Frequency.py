# PROBLEM NUMBER: 451
# https://leetcode.com/problems/sort-characters-by-frequency/
# 451.Sort Characters By Frequency
# DIFFICULTY: MEDIUM
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Approach:
        # We count the frequency of each character in the string.
        # Then we sort the characters in descending order of frequency.
        # Finally, we build the result by repeating each character
        # according to its frequency.

        # Using a frequency map ensures correctness, and sorting by
        # frequency gives the required order.
        

        from collections import Counter

        freq = Counter(s)
        chars = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)

        result = []
        for ch in chars:
            result.append(ch * freq[ch])

        return "".join(result)
