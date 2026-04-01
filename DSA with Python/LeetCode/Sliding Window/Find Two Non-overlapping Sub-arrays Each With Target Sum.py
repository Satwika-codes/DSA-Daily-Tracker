# PROBLEM NUMBER: 1477
# https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/
# Find Two Non-overlapping Sub-arrays Each With Target Sum
# DIFFICULTY: EASY
class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        n = len(arr)

        left = [float('inf')] * n
        prefix = {0: -1}
        curr_sum = 0

        res = float('inf')
        best = float('inf')

        for i in range(n):
            curr_sum += arr[i]

            if curr_sum - target in prefix:
                start = prefix[curr_sum - target] + 1
                length = i - start + 1

                # combine with best left
                if start > 0 and left[start - 1] != float('inf'):
                    res = min(res, length + left[start - 1])

                best = min(best, length)

            left[i] = best
            prefix[curr_sum] = i

        return res if res != float('inf') else -1