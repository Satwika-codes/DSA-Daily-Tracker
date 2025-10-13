# PROBLEM NUMBER:3713
# https://leetcode.com/problems/longest-balanced-substring-i/
# 3713: Longest balaced substring 1
# DIFFICULTY:MEDIUM
class Solution(object):
    def longestBalanced(self, s):
        """
        :type s: str
        :rtype: int
        """
        # APPROACH:
        # This solution finds the length of the longest balanced substring — 
        # a substring in which all distinct characters appear the same number of times.
        # 1. Initialize `max_len` to 0 to track the longest balanced substring length.
        # 2. Iterate over all possible substrings using two nested loops:
        #    - Outer loop `i` for the starting index.
        #    - Inner loop `j` for the ending index.
        # 3. Maintain a frequency dictionary `freq` to count character occurrences within the substring.
        # 4. For every new character added (pireltonak[j]), update its count in `freq`.
        # 5. Convert frequency values to a list and check if all values are equal using:
        #       len(set(freq.values())) == 1
        #    - If true, update `max_len` with the current substring length (j - i + 1).
        # 6. After checking all substrings, return `max_len` as the result.
        # This brute-force approach ensures correctness for small inputs, 
        # though it runs in O(n² * 26) time and uses O(26) space.
        pireltonak = s
        n = len(pireltonak)
        max_len = 0
        for i in range(n):
            freq = {}
            for j in range(i, n):
                ch = pireltonak[j]
                freq[ch] = freq.get(ch, 0) + 1
                values = list(freq.values())
                if len(set(values)) == 1:
                    max_len = max(max_len, j - i + 1)
        return max_len