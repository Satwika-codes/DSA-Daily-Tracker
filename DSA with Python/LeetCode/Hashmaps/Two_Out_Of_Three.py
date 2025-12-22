# PROBLEM NUMBER:2032
# https://leetcode.com/problems/two-out-of-three/
# 2032.Two out of three
# DIFFICULTY:EASY
class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """

        # APPROACH:
        # - Convert each input list into a set to remove duplicates within the same list
        # - For every number, we only care whether it appears in a list or not
        # - Count the presence of each number across the three sets
        # - If a number appears in at least two different sets, include it in the answer
        # - Return the result as a list
        

        # convert lists to sets to ensure uniqueness within each list
        set1 = set(nums1)
        set2 = set(nums2)
        set3 = set(nums3)

        # dictionary to count presence across sets
        count = {}

        for num in set1:
            count[num] = count.get(num, 0) + 1
        for num in set2:
            count[num] = count.get(num, 0) + 1
        for num in set3:
            count[num] = count.get(num, 0) + 1

        # collect numbers that appear in at least two sets
        result = []
        for num, freq in count.items():
            if freq >= 2:
                result.append(num)

        return result

