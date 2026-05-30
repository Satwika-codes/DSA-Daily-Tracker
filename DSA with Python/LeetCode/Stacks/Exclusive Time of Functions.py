# PROBLEM NUMBER: 636
# https://leetcode.com/problems/exclusive-time-of-functions/
# 636. Exclusive Time of Functions
# DIFFICULTY: MEDIUM

class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """

        # Approach:
        # We use a stack to simulate the function call stack.
        #
        # Exclusive Time:
        # Time spent inside a function excluding
        # the time consumed by functions it calls.
        #
        # Step 1:
        # Create:
        #
        # • res[i]
        #   Stores exclusive time of function i.
        #
        # • stack
        #   Stores currently active functions.
        #
        # • prev_time
        #   Tracks the beginning of the current
        #   execution interval.
        #
        # Step 2:
        # Traverse each log entry.
        #
        # Format:
        # "function_id:start/end:timestamp"
        #
        # Step 3:
        # If current log is "start":
        #
        # • If another function is running,
        #   add elapsed time to that function.
        #
        # • Push new function onto stack.
        #
        # • Update prev_time.
        #
        # Step 4:
        # If current log is "end":
        #
        # • Current function finishes execution.
        #
        # • Add:
        #   end_time - prev_time + 1
        #
        # • Pop function from stack.
        #
        # • Move prev_time to
        #   time + 1 because end timestamp
        #   is inclusive.
        #
        # Step 5:
        # Return exclusive execution times.

        res = [0] * n

        stack = []

        prev_time = 0

        for log in logs:

            fn, typ, time = log.split(':')

            fn = int(fn)
            time = int(time)

            # Function starts
            if typ == "start":

                # Previous function was running
                if stack:
                    res[stack[-1]] += time - prev_time

                # Start new function
                stack.append(fn)

                prev_time = time

            # Function ends
            else:

                # Add execution time
                res[stack.pop()] += time - prev_time + 1

                # Next interval starts after end time
                prev_time = time + 1

        return res