# PROBLEM NUMBER: 1640
# https://leetcode.com/problems/construct-array-by-concatenating-array
# Check Formation of Array Through Concatenation
# DIFFICULTY: EASY
class Solution(object):
    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        
        # APPROACH:
        # - Each piece must appear in the array as a contiguous subarray.
        # - The order of numbers inside each piece cannot be changed.
        # - Create a mapping from the first element of each piece to the piece itself.
        # - Traverse the array from left to right and try to match pieces greedily.
        

        first_map = {piece[0]: piece for piece in pieces}
        i = 0

        while i < len(arr):
            if arr[i] not in first_map:
                return False

            piece = first_map[arr[i]]
            for num in piece:
                if i >= len(arr) or arr[i] != num:
                    return False
                i += 1

        return True
