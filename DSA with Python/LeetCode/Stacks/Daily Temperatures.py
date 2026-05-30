# PROBLEM NUMBER: 739
# https://leetcode.com/problems/daily-temperatures/
# 739. Daily Temperatures
# DIFFICULTY: MEDIUM

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        # Approach:
        # We use a Monotonic Decreasing Stack
        # to find the next warmer day for each day.
        #
        # Step 1:
        # Create:
        #
        # • res = [0] * n
        #   Stores the number of days to wait
        #   for a warmer temperature.
        #
        # • stack
        #   Stores indices of days whose
        #   next warmer day has not been found yet.
        #
        # Step 2:
        # Traverse the temperatures array.
        #
        # Step 3:
        # While the current temperature is
        # greater than the temperature at the
        # index on the top of the stack:
        #
        # • We have found a warmer day.
        #
        # • Pop that index.
        #
        # • Calculate waiting days:
        #
        #   current_index - popped_index
        #
        # • Store the result.
        #
        # Step 4:
        # Push the current index into the stack.
        #
        # Step 5:
        # Any indices left in the stack
        # do not have a future warmer day,
        # so their answers remain 0.
        #
        # Step 6:
        # Return the result array.

        n = len(temperatures)

        res = [0] * n

        # Stores indices
        stack = []

        for i in range(n):

            # Found a warmer temperature
            while (
                stack and
                temperatures[i] > temperatures[stack[-1]]
            ):

                idx = stack.pop()

                res[idx] = i - idx

            # Store current index
            stack.append(i)

        return res