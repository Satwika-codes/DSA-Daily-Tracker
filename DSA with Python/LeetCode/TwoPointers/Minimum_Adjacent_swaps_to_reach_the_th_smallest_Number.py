# PROBLEM NUMBER: 1850
# https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/
# 1850.Minimum Adjacent swaps to reach the kth smallest Number
# DIFFICULTY: MEDIUM
class Solution(object):
    def getMinSwaps(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: int
        """
        # Approach:
        # 1. Create a copy of the original number as a list.
        # 2. Generate the k-th next lexicographical permutation using
        #    the standard next_permutation algorithm:
        #       - Find the first decreasing index from the right.
        #       - Find the next greater element to its right.
        #       - Swap them.
        #       - Reverse the suffix.
        # 3. After obtaining the target permutation, compute the
        #    minimum adjacent swaps required to convert the original
        #    list into the target list.
        # 4. Traverse left to right:
        #       - If elements differ, find the matching element ahead.
        #       - Move it left using adjacent swaps.
        #       - Count each swap.
        # 5. Return total swaps.

        # Time Complexity: O(k*n + n^2)
        # Space Complexity: O(n)

        def next_permutation(arr):
            # Step 1: find first decreasing element from right
            i = len(arr) - 2
            while i >= 0 and arr[i] >= arr[i + 1]:
                i -= 1
            
            # Step 2: find just larger element
            j = len(arr) - 1
            while arr[j] <= arr[i]:
                j -= 1
            
            # Step 3: swap
            arr[i], arr[j] = arr[j], arr[i]
            
            # Step 4: reverse suffix
            arr[i + 1:] = reversed(arr[i + 1:])
        
        original = list(num)
        target = list(num)
        
        # Get k-th permutation
        for _ in range(k):
            next_permutation(target)
        
        swaps = 0
        
        # Count minimum adjacent swaps
        for i in range(len(original)):
            if original[i] != target[i]:
                j = i
                while original[j] != target[i]:
                    j += 1
                
                # bring element to position i
                while j > i:
                    original[j], original[j - 1] = original[j - 1], original[j]
                    swaps += 1
                    j -= 1
        
        return swaps
