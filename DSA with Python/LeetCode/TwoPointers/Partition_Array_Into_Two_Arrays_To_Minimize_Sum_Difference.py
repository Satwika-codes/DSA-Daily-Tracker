# PROBLEM NUMBER:2035
# https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/
# 2035. Partition Array Into Two Arrays to Minimize Sum Difference
# DIFFICULTY:
class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """    
        # Approach:
        # This problem is solved using the "Meet in the Middle" technique.
        # 1. Split the array into two halves: left and right (each of size n).
        # 2. Compute all possible subset sums of the right half and group them
        #    based on how many elements are chosen.
        # 3. Sort these subset sums to enable binary search.
        # 4. For every subset of the left half:
        #    - Calculate its sum.
        #    - Determine how many elements must be chosen from the right half.
        #    - Use binary search to find the closest subset sum from the right
        #      that makes the total sum as close as possible to half of the total.
        # 5. Track the minimum absolute difference between the two subset sums.

        # Time Complexity:
        # ----------------
        # O(2^n * n), where n = len(nums) / 2

        # Space Complexity:
        # -----------------
        # O(2^n), for storing subset sums.
        

        n = len(nums) // 2
        left = nums[:n]
        right = nums[n:]
        total_sum = sum(nums)

        from itertools import combinations
        import bisect

        # Store sums of right half grouped by number of elements chosen
        right_sums = [[] for _ in range(n + 1)]

        for k in range(n + 1):
            for comb in combinations(right, k):
                right_sums[k].append(sum(comb))

        # Sort each list for binary search
        for k in range(n + 1):
            right_sums[k].sort()

        ans = float('inf')

        # Try all combinations of left half
        for k in range(n + 1):
            for comb in combinations(left, k):
                left_sum = sum(comb)
                need = total_sum / 2 - left_sum

                # We need (n - k) elements from right
                arr = right_sums[n - k]
                idx = bisect.bisect_left(arr, need)

                # Check closest sums
                for j in [idx - 1, idx]:
                    if 0 <= j < len(arr):
                        curr = left_sum + arr[j]
                        diff = abs(total_sum - 2 * curr)
                        ans = min(ans, diff)

        return ans