# PROBLEM NUMBER: 719
# https://leetcode.com/problems/find-k-th-smallest-pair-distance/
# 719. Find K-th Smallest Pair Distance
# DIFFICULTY: HARD
class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        Approach:
        The distance between a pair is the absolute difference of two numbers.
        First sort the array so pair distances are monotonic.
        Use binary search on the answer (distance d).
        For a guessed distance d, count how many pairs have distance <= d
        using a sliding window (two pointers).
        If the count is >= k, try smaller distances; otherwise try larger ones.
        The smallest distance for which at least k pairs exist is the answer.
        """

        nums.sort()
        n = len(nums)

        def count_pairs(max_dist):
            count = 0
            left = 0
            for right in range(n):
                while nums[right] - nums[left] > max_dist:
                    left += 1
                count += right - left
            return count

        low, high = 0, nums[-1] - nums[0]

        while low < high:
            mid = (low + high) // 2
            if count_pairs(mid) >= k:
                high = mid
            else:
                low = mid + 1

        return low
