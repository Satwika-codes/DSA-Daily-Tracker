# PROBLEM NUMBER: 2437
# https://leetcode.com/problems/remove-nodes-from-linked-list/
# 2437. Remove Nodes From Linked List
# DIFFICULTY: MEDIUM

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Approach:
        # We need to remove nodes that have a greater value node to their right.
        #
        # Step 1: Reverse the linked list:
        #         • So we can process from right → left
        #
        # Step 2: Traverse reversed list:
        #         • Keep track of maximum value seen so far (max_val)
        #
        # Step 3: For each node:
        #         • If next node value < max_val → remove it
        #         • Else → update max_val and move forward
        #
        # Step 4: Reverse the list again to restore original order
        #
        # Step 5: Return the final head

        # Step 1: reverse list
        head = self.reverse(head)

        # Step 2: remove nodes smaller than max
        max_val = head.val
        curr = head

        while curr and curr.next:
            if curr.next.val < max_val:
                curr.next = curr.next.next
            else:
                curr = curr.next
                max_val = curr.val

        # Step 3: reverse again
        return self.reverse(head)

    def reverse(self, head):
        # Standard linked list reversal
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev