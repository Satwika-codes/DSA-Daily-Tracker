# PROBLEM NUMBER: 1526
# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/
# 1526. Minimum Number of Increments on Subarrays to Form a Target Array
# DIFFICULTY: HARD

class Solution(object):
    def minNumberOperations(self, target):
        """
        :type target: List[int]
        :rtype: int
        """

        # Approach:
        # We start with an array of all zeros
        # and need to form the target array
        # using the minimum number of operations.
        #
        # One operation:
        # • Choose any subarray
        # • Increment every element in it by 1
        #
        # Key Insight:
        # Instead of thinking about operations,
        # think about how much "new height"
        # must be added at each position.
        #
        # Step 1:
        # The first element requires
        # target[0] operations because
        # we start from zero.
        #
        # Step 2:
        # Traverse the array from left to right.
        #
        # Step 3:
        # If current value is greater than
        # the previous value:
        #
        # • Extra height is needed.
        #
        # • Add:
        #
        #   target[i] - target[i - 1]
        #
        # to the answer.
        #
        # Step 4:
        # If current value is smaller than
        # or equal to the previous value:
        #
        # • No new operations are required.
        #
        # • Previous operations can already
        #   cover this position.
        #
        # Step 5:
        # Return the total operations.

        # Operations needed for first element
        ans = target[0]

        for i in range(1, len(target)):

            # Add only positive increases
            if target[i] > target[i - 1]:

                ans += target[i] - target[i - 1]

        return ans