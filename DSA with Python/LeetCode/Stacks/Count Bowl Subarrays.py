# PROBLEM: Bowl Subarrays
# PLATFORM: Custom / Coding Assessment Problem
# DIFFICULTY: MEDIUM

class Solution(object):
    def bowlSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Approach:
        # We use a Monotonic Decreasing Stack
        # to count valid bowl subarrays efficiently.
        #
        # Key Idea:
        # The stack maintains elements in
        # decreasing order.
        #
        # Step 1:
        # Traverse each element in the array.
        #
        # Step 2:
        # While the current element is greater
        # than the stack top:
        #
        # • Pop the smaller element.
        # • Increment answer.
        #
        # This accounts for valid bowl
        # relationships formed during popping.
        #
        # Step 3:
        # If the stack is not empty after popping:
        #
        # • Increment answer again because the
        #   current element forms another valid
        #   relationship with the remaining top.
        #
        # Step 4:
        # Push the current element into the stack.
        #
        # Step 5:
        # During counting, adjacent elements
        # are also included.
        #
        # • There are exactly (n - 1)
        #   adjacent pairs.
        #
        # • Subtract them from the final count
        #   to obtain the required answer.
        #
        # Step 6:
        # Return the result.

        stack = []
        ans = 0

        for x in nums:

            # Remove smaller elements
            while stack and stack[-1] < x:

                stack.pop()

                ans += 1

            # Form relation with remaining top
            if stack:

                ans += 1

            stack.append(x)

        # Remove adjacent pair contributions
        return ans - (len(nums) - 1)