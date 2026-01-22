# PROBLEM NUMBER: 1089
# https://leetcode.com/problems/duplicate-zeros/
# 1089. Duplicate Zeros
# DIFFICULTY: EASY
class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        # Approach:
        # First count how many zeros can be duplicated within array bounds.
        # Then traverse the array from the end and shift elements backward.
        # When a zero is encountered, write it twice if space permits.
        # This ensures in-place modification without extra space.    

        n = len(arr)
        zeros = 0
        
        for i in range(n):
            if i + zeros >= n:
                break
            if arr[i] == 0:
                if i + zeros == n - 1:
                    arr[n - 1] = 0
                    n -= 1
                    break
                zeros += 1
        
        last = n - 1 - zeros
        
        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + zeros] = 0
                zeros -= 1
                arr[i + zeros] = 0
            else:
                arr[i + zeros] = arr[i]
