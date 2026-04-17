# PROBLEM NUMBER: 116
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
# 116. Populating Next Right Pointers in Each Node
# DIFFICULTY: MEDIUM

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # Approach:
        # We need to connect nodes level by level using next pointers.
        # This version works for ANY binary tree (not necessarily perfect).
        #
        # Step 1: Start with current level pointer (curr = root)
        #
        # Step 2: For each level:
        #         • Use a dummy node to build the next level
        #         • tail pointer helps link nodes
        #
        # Step 3: Traverse current level using next pointers:
        #         • For each node:
        #             → If left child exists → connect it
        #             → If right child exists → connect it
        #
        # Step 4: Move curr using curr.next
        #
        # Step 5: After finishing level:
        #         • Move to next level → curr = dummy.next
        #
        # Step 6: Repeat until all levels processed
        #
        # Step 7: Return root

        curr = root

        while curr:
            dummy = Node(0)
            tail = dummy

            # traverse current level
            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next

                if curr.right:
                    tail.next = curr.right
                    tail = tail.next

                curr = curr.next

            # move to next level
            curr = dummy.next

        return root