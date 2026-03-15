# PROBLEMNUMBER: 350
# https://leetcode.com/problems/intersection-of-two-arrays-ii/
# 350. Intersection of Two Arrays II
# DIFFICULTY: EASY
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Approach:
        # We need to return the intersection of two arrays where each element in the
        # result should appear as many times as it shows in both arrays.
        
        # Idea:
        # Use a frequency dictionary to count occurrences of elements in nums1.
        
        # Step 1: Create a dictionary `freq` to store counts of each number in nums1.
        # Step 2: Traverse nums1 and update the frequency of each element.
        # Step 3: Traverse nums2 and check if the number exists in freq with count > 0.
        # Step 4: If yes:
        #         • Add the number to the result list
        #         • Decrease its frequency in the dictionary
        # Step 5: Continue until nums2 is processed.
        # Step 6: Return the result list.
        freq = {}
        result = []

        # Count elements in nums1
        for num in nums1:
            freq[num] = freq.get(num, 0) + 1

        # Check elements in nums2
        for num in nums2:
            if num in freq and freq[num] > 0:
                result.append(num)
                freq[num] -= 1

        return result