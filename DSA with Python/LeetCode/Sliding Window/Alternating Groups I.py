# PROBLEM NUMBER: 3206
# https://leetcode.com/problems/alternating-groups
# 3206.Alternating Groups
# DIFFICULTY: EASY
class Solution(object):
    def numberOfAlternatingGroups(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """

        # Approach:
        # We need to count groups of 3 consecutive elements (circularly)
        # such that they form an alternating pattern.
        #
        # Step 1: Let n be the length of the array.
        #
        # Step 2: Traverse each index i from 0 to n-1.
        #
        # Step 3: For each index, consider three consecutive elements:
        #         • a = colors[i]
        #         • b = colors[(i + 1) % n]
        #         • c = colors[(i + 2) % n]
        #         (Use modulo to handle circular wrapping.)
        #
        # Step 4: Check if the group is alternating:
        #         • a != b AND b != c
        #
        # Step 5: If the condition is satisfied, increment count.
        #
        # Step 6: Continue for all indices and return the total count.

        n = len(colors)
        count = 0

        for i in range(n):
            a = colors[i]
            b = colors[(i + 1) % n]
            c = colors[(i + 2) % n]

            if a != b and b != c:
                count += 1

        return count