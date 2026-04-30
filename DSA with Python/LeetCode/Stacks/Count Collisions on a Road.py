# PROBLEM NUMBER: 2211
# https://leetcode.com/problems/count-collisions-on-a-road/
# 2211. Count Collisions on a Road
# DIFFICULTY:MEDIUM
class Solution(object):
    def countCollisions(self, directions):
        """
        :type directions: str
        :rtype: int
        """
        # Approach:
        # We need to count total collisions between cars.
        #
        # Key Insight:
        # • Cars moving 'L' at the beginning will never collide
        # • Cars moving 'R' at the end will never collide
        # • Only the middle segment contributes to collisions
        #
        # Step 1: Use two pointers:
        #         • i from left
        #         • j from right
        #
        # Step 2: Skip all leading 'L':
        #         • They move away → no collision
        #
        # Step 3: Skip all trailing 'R':
        #         • They move away → no collision
        #
        # Step 4: Now consider subarray [i, j]:
        #         • All cars here will eventually stop or collide
        #
        # Step 5: Count all moving cars in this range:
        #         • 'L' and 'R' contribute to collisions
        #         • 'S' already stopped → no collision
        #
        # Step 6: Return total collisions

        i = 0
        j = len(directions) - 1

        # remove leading L
        while i <= j and directions[i] == 'L':
            i += 1

        # remove trailing R
        while i <= j and directions[j] == 'R':
            j -= 1

        collisions = 0

        for k in range(i, j + 1):
            if directions[k] != 'S':
                collisions += 1

        return collisions