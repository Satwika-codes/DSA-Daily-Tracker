# PROBLEM NUMBER: 1653
# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/
# 1653. Minimum Deletions to Make String Balanced
# DIFFICULTY: MEDIUM

class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Approach:
        # A balanced string should not contain
        # any 'b' before an 'a'.
        #
        # Traverse the string while counting
        # the number of 'b' characters seen so far.
        #
        # When we encounter an 'a', we have
        # two possible choices:
        #
        # • Delete the current 'a'
        # • Delete all previous 'b' characters
        #
        # We choose the option requiring fewer
        # deletions and update our answer.
        #
        # After processing the entire string,
        # the deletion count represents the
        # minimum removals needed.

        b_count = 0
        deletions = 0

        for ch in s:

            if ch == 'b':
                b_count += 1

            else:
                deletions = min(deletions + 1, b_count)

        return deletions