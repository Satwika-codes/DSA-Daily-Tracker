# PROBLEM NUMBER: 2570
# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/description/
# 2570. Merge Two 2D Arrays by Summing Values
# DIFFICULTY: EASY
class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        # Approach:
        # We need to merge two sorted 2D arrays where each element is [id, value].
        # If both arrays contain the same id, we sum their values.
        # Since both arrays are already sorted by id, we can use the two-pointer technique.
        
        # Step 1: Initialize two pointers:
        #         i → pointer for nums1
        #         j → pointer for nums2
        #         Also create an empty list "result" to store the merged output.
        
        # Step 2: Traverse both arrays while i < len(nums1) and j < len(nums2):
        #         • Extract id and value from both arrays.
        #         • If id1 == id2:
        #               Add [id1, val1 + val2] to result.
        #               Move both pointers forward.
        #         • If id1 < id2:
        #               Add nums1[i] to result and move pointer i.
        #         • Otherwise:
        #               Add nums2[j] to result and move pointer j.
        
        # Step 3: After the loop ends, one of the arrays may still have remaining elements.
        #         Append the remaining elements from nums1 (if any).
        
        # Step 4: Append the remaining elements from nums2 (if any).
        
        # Step 5: Return the merged result array.
        i = 0
        j = 0
        result = []

        while i < len(nums1) and j < len(nums2):
            id1, val1 = nums1[i]
            id2, val2 = nums2[j]

            if id1 == id2:
                result.append([id1, val1 + val2])
                i += 1
                j += 1
            elif id1 < id2:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1

        # Add remaining elements
        while i < len(nums1):
            result.append(nums1[i])
            i += 1

        while j < len(nums2):
            result.append(nums2[j])
            j += 1

        return result