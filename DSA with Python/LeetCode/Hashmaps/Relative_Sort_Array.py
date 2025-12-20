# PROBLEM NUMBER:1122
# https://leetcode.com/problems/relative-sort-array/
# 1122.Relative Sort Array
# DIFFICULTY : EASY
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        # APPROACH
        # Use a hashmap to count the frequency of each element in arr1
        # Iterate through arr2 and append elements to result based on their frequency
        # Remove used elements from the hashmap after processing
        # Collect remaining elements not present in arr2
        # Sort the remaining elements in ascending order
        # Append them to the result and return

        freq = {}
        for num in arr1:
            freq[num] = freq.get(num, 0) + 1

        result = []

        for num in arr2:
            result.extend([num] * freq[num])
            del freq[num]

        remaining = []
        for num in freq:
            remaining.extend([num] * freq[num])

        result.extend(sorted(remaining))
        return result
