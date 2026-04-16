# PROBLEM NUMBER: 109
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
# 109. Convert Sorted List to Binary Search Tree
# DIFFICULTY: MEDIUM

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        # Approach:
        # We need to convert a sorted linked list into a height-balanced BST.
        #
        # Step 1: Base cases:
        #         • If list is empty → return None
        #         • If single node → return TreeNode(head.val)
        #
        # Step 2: Find middle node of list:
        #         • Use slow & fast pointers
        #         • Middle node becomes root
        #
        # Step 3: Split the list:
        #         • Break link before middle (prev.next = None)
        #
        # Step 4: Create root node using middle value
        #
        # Step 5: Recursively build:
        #         • Left subtree from left half
        #         • Right subtree from right half
        #
        # Step 6: Return root

        if not head:
            return None

        # single node → root
        if not head.next:
            return TreeNode(head.val)

        # find middle
        prev = None
        slow = head
        fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # break left half
        if prev:
            prev.next = None

        root = TreeNode(slow.val)

        # build left and right
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)

        return root