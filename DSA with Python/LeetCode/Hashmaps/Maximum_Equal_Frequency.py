# PROBLEM NUMBER: 1224
# https://leetcode.com/problems/maximum-equal-frequency/
# 1224.Maximum Equal Frequency
# DIFFICULTY: HARD
class Solution(object):
    def maxEqualFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # APPROACH:
        # - We want the longest prefix where, after removing at most one element,
        #   all numbers have the same frequency.
        # - Maintain two hashmaps:
            # * freq[x]: frequency of number x
            # * count[f]: how many numbers currently have frequency f
        # - Track the maximum frequency seen so far.
        # - At each step, check if the current prefix is valid using these cases:
            # 1) All numbers appear once.
            # 2) Only one number has frequency 1 and the rest have the same frequency.
            # 3) Only one number has the maximum frequency and removing one occurrence
            #    makes all frequencies equal.
        # - Update the answer with the largest valid prefix length.
        

        from collections import defaultdict

        freq = defaultdict(int)
        count = defaultdict(int)
        max_freq = 0
        res = 0

        for i, num in enumerate(nums):
            prev = freq[num]
            if prev > 0:
                count[prev] -= 1

            freq[num] += 1
            curr = freq[num]
            count[curr] += 1
            max_freq = max(max_freq, curr)

            length = i + 1

            if (
                max_freq == 1 or
                max_freq * count[max_freq] + 1 == length or
                (max_freq - 1) * (count[max_freq - 1] + 1) == length
            ):
                res = length

        return res
