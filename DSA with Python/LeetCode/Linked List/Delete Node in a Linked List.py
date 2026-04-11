# PROBLEM NUMBER: 237
# https://leetcode.com/problems/delete-node-in-a-linked-list/
# 237. Delete Node in a Linked List
# DIFFICULTY: MEDIUM

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # Approach:
        # We are given only the node to be deleted (not the head).
        # We need to delete this node from the linked list.
        #
        # Step 1: Copy value of next node into current node:
        #         • node.val = node.next.val
        #
        # Step 2: Skip the next node:
        #         • node.next = node.next.next
        #
        # Step 3: This effectively removes the next node,
        #         and current node takes its place
        #
        # Step 4: No return needed (in-place modification)

        node.val = node.next.val
        node.next = node.next.next