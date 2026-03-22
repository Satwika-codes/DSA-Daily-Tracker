# PROBLEM NUMBER:978
# https://leetcode.com/problems/longest-turbulent-subarray/
# 978.Longest Turbulent Subarray
# DIFFICULTY:MEDIUM
class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
         # Approach:
        # We need to find the length of the longest subarray where
        # elements are in a "turbulent" pattern (alternating > and <).
        #
        # Step 1: If array length < 2, return n directly.
        #
        # Step 2: Initialize:
        #         • curr → current turbulent subarray length
        #         • max_len → maximum length found so far
        #
        # Step 3: Traverse the array from index 1 to n-1.
        #
        # Step 4: For i == 1:
        #         • If arr[1] != arr[0], curr = 2
        #         • Else, curr = 1
        #
        # Step 5: For i >= 2:
        #         • Check if pattern alternates:
        #           (arr[i-2] < arr[i-1] > arr[i]) OR
        #           (arr[i-2] > arr[i-1] < arr[i])
        #           → If yes, increase curr by 1
        #
        #         • Else if arr[i] != arr[i-1]:
        #           → Start new turbulent subarray of length 2
        #
        #         • Else:
        #           → Reset curr = 1
        #
        # Step 6: Update max_len with the maximum value of curr.
        #
        # Step 7: Return max_len.
        n = len(arr)
        if n < 2:
            return n

        max_len = 1
        curr = 1

        for i in range(1, n):
            if i == 1:
                if arr[i] != arr[i - 1]:
                    curr = 2
                else:
                    curr = 1
            else:
                if (arr[i-2] < arr[i-1] > arr[i]) or (arr[i-2] > arr[i-1] < arr[i]):
                    curr += 1
                elif arr[i] != arr[i-1]:
                    curr = 2
                else:
                    curr = 1

            max_len = max(max_len, curr)

        return max_len
        