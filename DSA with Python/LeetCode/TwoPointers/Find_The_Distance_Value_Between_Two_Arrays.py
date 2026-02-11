# PROBLEM NUMBER:1385
# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/
# 1385. Find the Distance Value Between Two Arrays
# DIFFICULTY:EASY
import bisect
class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        # Approach:
        # 1. Sort arr2.
        # 2. For each element x in arr1:
        #    - Use binary search to find insertion position in arr2.
        #    - Check neighbors around that position.
        #    - If any value is within distance d → invalid.
        # 3. Count valid elements.

        # Time Complexity: O(n log n)
        # Space Complexity: O(1)
        
        arr2.sort()
        count = 0

        for x in arr1:
            pos = bisect.bisect_left(arr2, x)

            valid = True

            # Check left neighbor
            if pos > 0 and abs(x - arr2[pos - 1]) <= d:
                valid = False

            # Check right neighbor
            if pos < len(arr2) and abs(x - arr2[pos]) <= d:
                valid = False

            if valid:
                count += 1

        return count
