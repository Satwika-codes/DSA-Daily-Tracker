# PROBLEM NUMBER:2444
# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/
# 2444.Count Subarrays With Fixed Bounds.py
# DIFFICULTY:HARD
class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
        # Approach:
        # We need to count subarrays such that:
        # • The minimum element in the subarray is minK
        # • The maximum element in the subarray is maxK
        # Instead of checking all subarrays (which is costly),
        # we track positions of important elements while iterating.
        # Step 1: Maintain three indices:
        #         • lastMin → last index where minK appeared
        #         • lastMax → last index where maxK appeared
        #         • lastBad → last index where element was invalid(i.e., num < minK or num > maxK)
        # Step 2: Iterate through the array.
        # Step 3: If current element is invalid:
        #         • Update lastBad to current index
        # Step 4: If element equals minK:
        #         • Update lastMin
        # Step 5: If element equals maxK:
        #         • Update lastMax
        # Step 6: To count valid subarrays ending at current index i:
        #         • Take the minimum of lastMin and lastMax
        #           (this ensures both minK and maxK are included)
        # Step 7: If this position is after lastBad:
        #         • Add (valid_end - lastBad) to result
        #           → gives number of valid subarrays ending at i
        # Step 8: Return the total count

        lastMin = -1
        lastMax = -1
        lastBad = -1

        res = 0

        for i, num in enumerate(nums):

            # invalid element
            if num < minK or num > maxK:
                lastBad = i

            if num == minK:
                lastMin = i

            if num == maxK:
                lastMax = i

            # count valid subarrays ending at i
            valid_end = min(lastMin, lastMax)
            if valid_end > lastBad:
                res += valid_end - lastBad

        return res