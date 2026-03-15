# PROBLEM NUMBER: 1471
# https://leetcode.com/problems/the-k-strongest-values-in-an-array/
# 1471. The k Strongest Values in an Array
# DIFFICULTY: MEDIUM
class Solution(object):
    def getStrongest(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Approach:
        # Step 1: The goal is to find the `k` strongest elements in the array where strength is defined by the absolute difference between the element and the median of the array.
        # Step 2: First sort the array so that we can easily determine the median and use a two-pointer technique.
        # Step 3: Compute the median using the formula `arr[(n - 1) // 2]` after sorting, which represents the middle element according to the problem definition.
        # Step 4: Initialize two pointers: `left` at the start of the array and `right` at the end, along with an empty list `result` to store the strongest elements.
        # Step 5: While we still need to pick `k` elements, compute the strength of the elements at both pointers using `abs(arr[left] - median)` and `abs(arr[right] - median)`.
        # Step 6: Compare the two strengths and choose the element with the greater strength because it is considered stronger.
        # Step 7: If the right element is stronger, append it to the result and move the `right` pointer one step left.
        # Step 8: If the left element is stronger, append it to the result and move the `left` pointer one step right.
        # Step 9: If both elements have equal strength, choose the larger value as the stronger one according to the problem rule.
        # Step 10: Decrease `k` after selecting each element and continue until `k` elements have been collected.
        # Step 11: Finally return the list containing the `k` strongest elements.

        arr.sort()
        n = len(arr)
        median = arr[(n - 1) // 2]

        left = 0
        right = n - 1
        result = []

        while k > 0:
            left_strength = abs(arr[left] - median)
            right_strength = abs(arr[right] - median)

            if right_strength > left_strength:
                result.append(arr[right])
                right -= 1
            elif right_strength < left_strength:
                result.append(arr[left])
                left += 1
            else:  # equal strength → pick larger value
                if arr[right] > arr[left]:
                    result.append(arr[right])
                    right -= 1
                else:
                    result.append(arr[left])
                    left += 1

            k -= 1

        return result