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
        # We need to connect nodes at the same level using next pointers.
        # Given a perfect binary tree, we can solve this without extra space.
        #
        # Step 1: Handle edge case:
        #         • If root is None → return None
        #
        # Step 2: Start from leftmost node of each level
        #
        # Step 3: For each level:
        #         • Traverse nodes using next pointers (already connected)
        #
        # Step 4: For each node (curr):
        #         • Connect left child to right child
        #           → curr.left.next = curr.right
        #
        # Step 5: Connect across subtrees:
        #         • If curr has next:
        #           → curr.right.next = curr.next.left
        #
        # Step 6: Move curr using curr.next
        #
        # Step 7: After finishing current level:
        #         • Move to next level → leftmost = leftmost.left
        #
        # Step 8: Repeat until last level
        #
        # Step 9: Return root

        if not root:
            return None

        leftmost = root

        while leftmost.left:
            curr = leftmost

            while curr:
                # connect left -> right
                curr.left.next = curr.right

                # connect right -> next left
                if curr.next:
                    curr.right.next = curr.next.left

                curr = curr.next

            leftmost = leftmost.left

        return root