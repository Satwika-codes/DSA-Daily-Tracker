# PROBLEM NUMBER: 2122
# https://leetcode.com/problems/recover-the-original-array
# Recover The Original Array
# DIFFICULTY: HARD
class Solution(object):
    def recoverArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Approach:
        # The given array nums contains elements of the form:
        # original[i] - k and original[i] + k for some unknown k > 0.

        # Steps:
        # 1. Sort nums.
        # 2. The smallest element must be (x - k). Try pairing it with
        #    another element (x + k) to determine k.
        # 3. For each possible k candidate:
        #    - Use a frequency map (multiset).
        #    - Greedily pair smallest unused value a with (a + 2k).
        #    - If pairing fails, discard this k.
        # 4. When all elements are successfully paired, reconstruct
        #    the original array as a + k.

        # Only one valid k will work.
        

        from collections import Counter

        nums.sort()
        freq = Counter(nums)
        n = len(nums)

        for i in range(1, n):
            diff = nums[i] - nums[0]
            if diff <= 0 or diff % 2 != 0:
                continue

            k = diff // 2
            freq_copy = freq.copy()
            original = []

            valid = True
            for x in nums:
                if freq_copy[x] == 0:
                    continue
                if freq_copy[x + 2 * k] == 0:
                    valid = False
                    break
                freq_copy[x] -= 1
                freq_copy[x + 2 * k] -= 1
                original.append(x + k)

            if valid and len(original) * 2 == n:
                return original

        return []
