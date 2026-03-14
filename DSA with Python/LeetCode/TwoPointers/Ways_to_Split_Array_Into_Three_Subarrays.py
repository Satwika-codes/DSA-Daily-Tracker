class Solution(object):
    def waysToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach:
        # Step 1: The goal is to count the number of ways to split the array into three non-empty parts (left, middle, right) such that left_sum <= mid_sum <= right_sum.
        # Step 2: First compute the prefix sum array so that the sum of any subarray can be calculated quickly. Each element `prefix[i]` stores the sum of elements from index 0 to i.
        # Step 3: Store the total sum of the array using the last value of the prefix array and initialize a variable `result` to count valid splits.
        # Step 4: Fix the end index `i` of the left subarray and iterate from 0 to n-3 because the middle and right parts must contain at least one element each.
        # Step 5: For each `i`, compute `left_sum` as `prefix[i]`.
        # Step 6: The middle subarray will end at index `j`, and its sum is `prefix[j] - prefix[i]`. For the condition `mid_sum >= left_sum`, this becomes `prefix[j] >= 2 * left_sum`.
        # Step 7: Use binary search (`bisect_left`) to find the smallest index `low` where `prefix[j]` satisfies this condition within the valid range.
        # Step 8: For the condition `mid_sum <= right_sum`, transform it into `prefix[j] <= (total + left_sum) // 2`.
        # Step 9: Use another binary search (`bisect_right`) to find the largest index `high` satisfying this condition, subtracting 1 because `bisect_right` returns the insertion position.
        # Step 10: If `low <= high`, it means all indices between them produce valid splits, so add `(high - low + 1)` to the result.
        # Step 11: Continue checking all possible left partition positions.
        # Step 12: Finally return the result modulo `10^9 + 7` as required by the problem constraints.

        MOD = 10**9 + 7
        n = len(nums)

        # Step 1: Prefix sum
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]

        total = prefix[-1]
        result = 0

        # Step 2: Fix left end index i
        for i in range(n - 2):

            left_sum = prefix[i]

            # Lower bound: mid_sum >= left_sum
            # prefix[j] - prefix[i] >= left_sum
            # prefix[j] >= 2 * left_sum
            low = bisect.bisect_left(prefix, 2 * left_sum, i + 1, n - 1)

            # Upper bound: mid_sum <= right_sum
            # prefix[j] - prefix[i] <= total - prefix[j]
            # prefix[j] <= (total + prefix[i]) // 2
            high = bisect.bisect_right(prefix, (total + left_sum) // 2, i + 1, n - 1) - 1

            if low <= high:
                result += (high - low + 1)

        return result % MOD