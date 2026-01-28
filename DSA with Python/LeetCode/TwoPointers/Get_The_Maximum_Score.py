# PROBLEM NUMBER: 1537
# https://leetcode.com/problems/get-the-maximum-score
# 1357. Get The Maximum Score
# DIFFICULTY: HARD
class Solution(object):
    def maxSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # Approach:
        # ---------
        # This problem can be solved using a two-pointer technique since both
        # arrays are sorted.

        # We traverse both arrays simultaneously while maintaining two running
        # sums:
        # - s1: sum of elements taken from nums1
        # - s2: sum of elements taken from nums2

        # While traversing:
        # - If nums1[i] < nums2[j], we add nums1[i] to s1 and move pointer i.
        # - If nums1[i] > nums2[j], we add nums2[j] to s2 and move pointer j.
        # - If nums1[i] == nums2[j], this is a common element where we can
        #   choose to switch paths. We add max(s1, s2) plus the common element
        #   to the answer, reset both sums, and move both pointers.

        # After the main traversal, one array may still have remaining elements.
        # We add the remaining elements to the corresponding sum and finally
        # add max(s1, s2) to the answer.

        # The result is returned modulo 10^9 + 7.

        # Time Complexity: O(n + m)
        # Space Complexity: O(1)
        

        MOD = 10**9 + 7
        
        i = j = 0
        s1 = s2 = 0
        ans = 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                s1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                s2 += nums2[j]
                j += 1
            else:
                ans += max(s1, s2) + nums1[i]
                s1 = s2 = 0
                i += 1
                j += 1
        
        while i < len(nums1):
            s1 += nums1[i]
            i += 1
        
        while j < len(nums2):
            s2 += nums2[j]
            j += 1
        
        ans += max(s1, s2)
        
        return ans % MOD

        
        
                                         
