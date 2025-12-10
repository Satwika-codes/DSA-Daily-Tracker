# PROBLEM NUMBER: 1122
# https://leetcode.com/problems/relative-sort-array/
# 1122. Relative Sort Array
# DIFFICULTY: EASY
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """

        # Approach:
        # We want to reorder arr1 so that:
        #   1. Elements appear in the same order as arr2 (for all elements present in arr2)
        #   2. Remaining elements not in arr2 appear at the end in sorted order.
        #
        # Steps:
        # 1. Count the frequency of each number in arr1 using a dictionary.
        # 2. For every number in arr2:
        #       - Add it to the result as many times as it appears in arr1.
        #       - Remove it from the count map.
        #
        # 3. Whatever numbers remain in the dictionary are those **not in arr2**.
        #    Expand them according to frequency into a separate list.
        #
        # 4. Sort this remaining list.
        #
        # 5. Final result = numbers placed according to arr2 + sorted leftovers.
        #
        # Time Complexity: O(n log n) due to sorting leftover elements.
        # Space Complexity: O(n)

        count = {}
        for num in arr1:
            count[num] = count.get(num, 0) + 1
        
        res = []
        for num in arr2:
            if num in count:
                res.extend([num] * count[num])
                del count[num]
        
        rest = []
        for num in count:
            rest.extend([num] * count[num])
        
        return res + sorted(rest)
