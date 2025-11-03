# PROBLEM NUMBER: 306
# https://leetcode.com/problems/additive-number/
# 306. Additive Number
# DIFFICULTY: MEDIUM
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        # Approach:
        # 1. The goal is to check if a given numeric string can form an additive sequence.
        #    (An additive sequence means each number is the sum of the previous two.)
        # 2. Iterate over all possible splits for the first two numbers:
        #       - `a = num[:i]` → first number
        #       - `b = num[i:j]` → second number
        #    Ensure no number has leading zeros (unless it’s '0').
        # 3. Define a helper function `is_valid(a, b, start)`:
        #       - Continually generate the next expected number `c = str(int(a) + int(b))`.
        #       - Check if `num` starts with `c` from the current `start` position.
        #       - If mismatch occurs, return False.
        #       - Otherwise, move `start` forward and repeat with updated `a, b`.
        #       - If we reach the end successfully → True.
        # 4. For each valid (a, b) pair:
        #       - If `is_valid(a, b, j)` returns True → sequence is additive.
        # 5. If no valid pair found → return False.
        # Time Complexity: O(n³)  # Two nested loops + substring checks
        # Space Complexity: O(1)
        n = len(num)
        def is_valid(a, b, start):
            while start < n:
                c = str(int(a) + int(b))
                if not num.startswith(c, start):
                    return False
                start += len(c)
                a, b = b, c
            return True

        for i in range(1, n):
            for j in range(i + 1, n):
                a, b = num[:i], num[i:j]
                if (len(a) > 1 and a[0] == '0') or (len(b) > 1 and b[0] == '0'):
                    continue
                if is_valid(a, b, j):
                    return True
        return False