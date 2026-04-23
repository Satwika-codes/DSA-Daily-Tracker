# PROBLEM NUMBER: 1541
# https://leetcode.com/problems/minimum-additions-to-make-valid-string/
# 1541. Minimum Additions to Make Valid String
# DIFICULTY: MEDIUM

class Solution(object):
    def addMinimum(self, word):
        """
        :type word: str
        :rtype: int
        """
        # Approach:
        # We want to transform the string into repeating "abc" patterns
        # by inserting minimum characters.
        #
        # Key Idea:
        # • Each valid group should follow increasing order: 'a' → 'b' → 'c'
        # • If order breaks → a new "abc" group starts
        #
        # Step 1: Initialize groups = 1
        #         • At least one group exists
        #
        # Step 2: Traverse string:
        #         • If current char <= previous char:
        #             → order breaks
        #             → start new group (groups += 1)
        #
        # Step 3: Total characters needed:
        #         • Each group ideally has 3 chars ("abc")
        #         • So total = groups * 3
        #
        # Step 4: Characters already present = len(word)
        #
        # Step 5: Insertions needed:
        #         → (groups * 3) - len(word)
        #
        # Step 6: Return result

        groups = 1

        for i in range(1, len(word)):
            if word[i] <= word[i - 1]:
                groups += 1

        return groups * 3 - len(word)