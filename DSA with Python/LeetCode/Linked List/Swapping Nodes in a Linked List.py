# PROBLEM NUMBER: 1721
# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
# 1721. Swapping Nodes in a Linked List
# DIFFICULTY: MEDIUM

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        # Approach:
        # We need to find the next greater value for each node in the linked list.
        #
        # Step 1: Convert linked list into an array:
        #         • Easier to access elements by index
        #
        # Step 2: Initialize result array with 0s
        #         • Default value = 0 (if no greater element exists)
        #
        # Step 3: Use a monotonic decreasing stack:
        #         • Store indices of elements
        #         • Stack maintains decreasing order of values
        #
        # Step 4: Traverse the array:
        #         • For each index i:
        #           → While current value > value at stack top:
        #               • Pop index from stack
        #               • Set result for that index as current value
        #
        # Step 5: Push current index onto stack
        #
        # Step 6: Remaining indices in stack have no greater element
        #         • Their result remains 0
        #
        # Step 7: Return result array

        # Step 1: convert to array
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        res = [0] * len(nums)
        stack = []  # stores indices

        # Step 2: monotonic stack
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                idx = stack.pop()
                res[idx] = nums[i]
            stack.append(i)

        return res