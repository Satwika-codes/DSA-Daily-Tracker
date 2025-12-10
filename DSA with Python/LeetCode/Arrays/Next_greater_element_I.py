# PROBLEM NUMBER: 496
# https://leetcode.com/problems/next-greater-element-i/
# 496. Next Greater Element I
# DIFFICULTY: MEDIUM
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        # Approach:
        # We want to find the Next Greater Element (NGE) for each number in nums2.
        # A monotonic decreasing stack is used:
        #
        # 1. Traverse nums2:
        #    - While stack is not empty AND current number > stack top:
        #         → current number is the next greater element for the stack top.
        #         → Pop from stack and store this mapping.
        #
        # 2. After traversal, all remaining stack elements have no NGE:
        #         → map them to -1
        #
        # 3. Finally, for each element in nums1, return its mapped NGE.
        #
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        stack = []
        nge = {}

        for num in nums2:
            while stack and num > stack[-1]:
                nge[stack.pop()] = num
            stack.append(num)

        # Remaining numbers have no next greater element
        while stack:
            nge[stack.pop()] = -1

        return [nge[x] for x in nums1]
