# PROBLEM NUMBER: 821
# https://leetcode.com/problems/shortest-distance-to-a-character/
# 821. Shortest Distance to a Character
# DIFFICULTY: EASY
class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        # Approach:
        # 1. Create result array initialized with large values.
        # 2. Left → Right pass:
        #    - Keep track of last seen index of c.
        #    - Update distance.
        # 3. Right → Left pass:
        #    - Again track last seen index of c.
        #    - Take minimum of existing and new distance.

        # Time Complexity: O(n)
        # Space Complexity: O(n)

        n = len(s)
        result = [float('inf')] * n

        # Left to right
        prev = -float('inf')
        for i in range(n):
            if s[i] == c:
                prev = i
            result[i] = i - prev

        # Right to left
        prev = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            result[i] = min(result[i], prev - i)

        return result
