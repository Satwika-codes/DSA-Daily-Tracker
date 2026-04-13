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
    def isSubPath(self, head, root):
        """
        :type head: Optional[ListNode]
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # Approach:
        # We need to check if the linked list exists as a downward path in the tree.
        #
        # Step 1: For every node in the tree:
        #         • Try to match the linked list starting from that node
        #
        # Step 2: At each tree node:
        #         • Either start matching from here
        #         • Or recursively check left and right subtree
        #
        # Step 3: Use helper function (match):
        #         • Checks if linked list matches a path starting at current node
        #
        # Step 4: In match function:
        #         • If head is None → full list matched → return True
        #         • If node is None → path ended → return False
        #
        # Step 5: If values match:
        #         • Move to next list node
        #         • Try both left and right child (tree branching)
        #
        # Step 6: If values don’t match → return False
        #
        # Step 7: Return True if any path matches

        if not root:
            return False

        # check from current node OR move to children
        return (self.match(head, root) or
                self.isSubPath(head, root.left) or
                self.isSubPath(head, root.right))

    def match(self, head, node):
        # Step 8: If list fully matched
        if not head:
            return True

        # Step 9: If tree ends before list
        if not node:
            return False

        # Step 10: If values don't match
        if head.val != node.val:
            return False

        # Step 11: Continue matching in both directions
        return (self.match(head.next, node.left) or
                self.match(head.next, node.right))