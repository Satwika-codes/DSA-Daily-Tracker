# PROBLEM NUMBER: 1770
# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/
# 1770.Number of Subsequences That Satisfy the Given Sum Condition
# DIFFICULTY: HARD
class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Approach:
        # Step 1: The goal is to count the number of subsequences such that the sum of the minimum and maximum elements in the subsequence is less than or equal to the given target.
        # Step 2: First sort the array so that we can efficiently apply the two-pointer technique to control the minimum and maximum elements.
        # Step 3: Precompute powers of 2 in an array `power` where power[i] represents 2^i modulo (10^9 + 7). This helps count the number of possible subsequences between two pointers.
        # Step 4: Use two pointers: `left` starting at the beginning of the array and `right` starting at the end.
        # Step 5: While `left` is less than or equal to `right`, check whether the sum of the smallest and largest elements (`nums[left] + nums[right]`) is less than or equal to the target.
        # Step 6: If the condition is satisfied, it means all subsequences formed using `nums[left]` as the minimum and any subset of elements between `left` and `right` are valid.
        # Step 7: The number of such subsequences is 2^(right - left), so add `power[right - left]` to the result and move the `left` pointer forward.
        # Step 8: If the condition is not satisfied, decrease the `right` pointer to reduce the maximum element and try again.
        # Step 9: Continue this process until the two pointers cross each other.
        # Step 10: Return the final result modulo (10^9 + 7) to handle large counts.
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)

        # Precompute powers of 2
        power = [1] * n
        for i in range(1, n):
            power[i] = (power[i - 1] * 2) % MOD

        left, right = 0, n - 1
        result = 0

        while left <= right:
            if nums[left] + nums[right] <= target:
                result = (result + power[right - left]) % MOD
                left += 1
            else:
                right -= 1

        return result