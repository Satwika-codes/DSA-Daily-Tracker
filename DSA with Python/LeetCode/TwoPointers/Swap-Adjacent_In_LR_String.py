# PROBLEM NUMBER:777
# https://leetcode.com/problems/swap-adjacent-in-lr-string/
# 777. Swap Adjacent in LR String
# DIFFICULTY:MEDIUM
class Solution(object):
    def canTransform(self, start, result):
        """
        :type start: str
        :type result: str
        :rtype: bool
        """
        # Approach:
        # This problem checks whether we can transform the string `start`
        # into `result` by swapping only adjacent characters, where:
        # - 'L' can move ONLY to the left
        # - 'R' can move ONLY to the right
        # - 'X' represents an empty space

        # Steps:
        # 1. Length Check:
        #    If the lengths of `start` and `result` are different,
        #    transformation is impossible.

        # 2. Order Check:
        #    Remove all 'X' characters from both strings.
        #    The relative order of 'L' and 'R' must remain the same,
        #    otherwise transformation is not possible.

        # 3. Two Pointer Traversal:
        #    - Use two pointers to scan both strings.
        #    - Skip 'X' characters.
        #    - For each matching 'L' or 'R':
        #      • 'L' must NOT move to the right.
        #      • 'R' must NOT move to the left.
        #    If any rule is violated, return False.

        # If all checks pass, return True.

        # :type start: str
        # :type result: str
        # :rtype: bool
        

        # 1 Length must be same
        if len(start) != len(result):
            return False

        # 2 Order of L and R must be same (ignore X)
        if start.replace('X', '') != result.replace('X', ''):
            return False

        # 3 Check movement constraints
        i = j = 0
        n = len(start)

        while i < n and j < n:
            # Skip X in both strings
            while i < n and start[i] == 'X':
                i += 1
            while j < n and result[j] == 'X':
                j += 1

            if i == n or j == n:
                break

            # If characters mismatch
            if start[i] != result[j]:
                return False

            # L can only move left
            if start[i] == 'L' and i < j:
                return False

            # R can only move right
            if start[i] == 'R' and i > j:
                return False

            i += 1
            j += 1

        return True
