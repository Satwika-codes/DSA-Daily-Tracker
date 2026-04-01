class Solution(object):
    def maxFrequencyScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Approach:
        # We need to find the maximum size subarray such that we can make
        # all its elements equal using at most k operations.
        #
        # Operation: Increase or decrease elements to make them equal.
        #
        # Step 1: Sort the array.
        #         • This helps us group close elements together
        #         • Makes it easier to convert all elements to a common value
        #
        # Step 2: Use prefix sum array to quickly calculate range sums.
        #         • prefix[i] stores sum of first i elements
        #
        # Step 3: Use sliding window with two pointers (left, right)
        #
        # Step 4: For each window [left, right]:
        #         • Choose median (mid) as target value
        #           → minimizes total cost to make all elements equal
        #
        # Step 5: Calculate cost to convert all elements in window to nums[mid]:
        #
        #         • Left side cost:
        #           nums[mid] * (mid - left) - (sum of left part)
        #
        #         • Right side cost:
        #           (sum of right part) - nums[mid] * (right - mid)
        #
        #         • Total cost = left_cost + right_cost
        #
        # Step 6: If total cost > k:
        #         • Shrink window from left
        #
        # Step 7: Otherwise:
        #         • Update result with current window size
        #
        # Step 8: Return maximum size found

        nums.sort()
        n = len(nums)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        res = 1
        left = 0

        for right in range(n):
            while left <= right:
                mid = (left + right) // 2

                # cost to make all = nums[mid]
                left_cost = nums[mid] * (mid - left) - (prefix[mid] - prefix[left])
                right_cost = (prefix[right + 1] - prefix[mid + 1]) - nums[mid] * (right - mid)

                total_cost = left_cost + right_cost

                if total_cost <= k:
                    break
                left += 1

            res = max(res, right - left + 1)

        return res