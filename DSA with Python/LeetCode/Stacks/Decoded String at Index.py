# PROBLEM NUMBER: 880
# https://leetcode.com/problems/decoded-string-at-index/
# 880. Decoded String at Index
# DIFFICULTY: MEDIUM

class Solution(object):
    def decodeAtIndex(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        # Approach:
        # Instead of constructing the fully
        # decoded string, first calculate its
        # total length.
        #
        # Letters increase the length by 1,
        # while digits repeat the current
        # decoded string multiple times.
        #
        # After finding the total size,
        # traverse the string in reverse.
        #
        # Use k %= size to map the required
        # position back into the previous
        # decoded string before expansion.
        #
        # When a letter is reached and
        # k becomes 0, that letter is the
        # answer.

        size = 0

        for ch in s:

            if ch.isdigit():
                size *= int(ch)

            else:
                size += 1

        for ch in reversed(s):

            k %= size

            if ch.isalpha():

                if k == 0:
                    return ch

                size -= 1

            else:

                size //= int(ch)