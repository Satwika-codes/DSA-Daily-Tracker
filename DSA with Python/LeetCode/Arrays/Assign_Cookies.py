# PROBLEM NUMBER: 455
# https://leetcode.com/problems/assign-cookies/
# 455.Assign Cookies
# DIFFICULTY: EASY
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """

        # Problem:
        # Each child has a greed factor g[i] (minimum cookie size required).
        # Each cookie has a size s[j].
        # Assign at most one cookie to each child. Count how many children can be satisfied.

        # Approach: Greedy + Sorting
        #
        # 1. Sort both greed list (g) and cookie size list (s).
        # 2. Use two pointers:
        #       i -> child index
        #       j -> cookie index
        # 3. For each cookie:
        #       - If the current cookie s[j] is enough to satisfy child g[i],
        #         assign cookie → increment both pointers + count.
        #       - Otherwise, try next larger cookie → j += 1
        #
        # Reason Greedy Works:
        # - Always satisfy the least greedy child first with the smallest possible cookie.
        # - This maximizes the total satisfied children.
        #
        # Time Complexity: O(n log n + m log m) due to sorting
        # Space Complexity: O(1) extra

        g.sort()
        s.sort()

        i = j = 0   # i = child pointer, j = cookie pointer
        count = 0

        while i < len(g) and j < len(s):

            # If cookie size is enough for current child
            if s[j] >= g[i]:
                count += 1
                i += 1
                j += 1
            else:
                # Cookie too small → try next larger cookie
                j += 1

        return count
