# PROBLEM NUMBER: 1652
# https://leetcode.com/problems/defuse-the-bomb/
# 1652. Defuse the Bomb
# DIFFICULTY: MEDIUM
class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Approach:
        # We need to replace each element with the sum of next k elements (if k > 0)
        # or previous k elements (if k < 0) in a circular array.
        #
        # Step 1: If k == 0:
        #         • All elements become 0 → return result array
        #
        # Step 2: Use sliding window to maintain sum of k elements
        #
        # Step 3: Define initial window:
        #         • If k > 0 → window is next k elements → [1 to k]
        #         • If k < 0 → window is previous k elements → [n+k to n-1]
        #
        # Step 4: Compute initial window sum using modulo for circular behavior
        #
        # Step 5: For each index i:
        #         • Assign current window_sum to res[i]
        #
        # Step 6: Slide the window:
        #         • Remove element at left
        #         • Add next element at right
        #         • Use modulo to wrap around circular array
        #
        # Step 7: Repeat for all indices
        #
        # Step 8: Return result array

        n = len(code)
        res = [0] * n

        if k == 0:
            return res

        window_sum = 0

        # define window range
        if k > 0:
            left, right = 1, k
        else:
            left, right = n + k, n - 1

        # initial window sum
        for i in range(left, right + 1):
            window_sum += code[i % n]

        for i in range(n):
            res[i] = window_sum

            # slide window
            window_sum -= code[left % n]
            left += 1

            right += 1
            window_sum += code[right % n]

        return res