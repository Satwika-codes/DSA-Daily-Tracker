# PROBLEM NUMBER: 845
# https://leetcode.com/problems/longest-mountain-in-an-array/
# 845. Longest Mountain in an Array
# DIFFICULTY: MEDIUM
class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # Approach:
        # A mountain requires a strictly increasing sequence followed by
        # a strictly decreasing sequence, with at least 3 elements.
        # Traverse the array and treat each index as a possible peak.
        # A valid peak satisfies arr[i-1] < arr[i] > arr[i+1].
        # From a peak, expand left while values increase and expand right
        # while values decrease, then update the maximum length.
        

        n = len(arr)
        ans = 0
        i = 1
        
        while i < n - 1:
            if arr[i - 1] < arr[i] > arr[i + 1]:
                l = i - 1
                r = i + 1
                
                while l > 0 and arr[l - 1] < arr[l]:
                    l -= 1
                while r < n - 1 and arr[r] > arr[r + 1]:
                    r += 1
                
                ans = max(ans, r - l + 1)
                i = r
            else:
                i += 1
        
        return ans
