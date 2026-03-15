# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # Approach:
        # We remove the Nth node from the end of the linked list using the two-pointer technique.
        
        # Idea:
        # Maintain a gap of n nodes between two pointers (fast and slow).
        # When fast reaches the end, slow will be just before the node we want to remove.
        
        # Step 1: Create a dummy node pointing to head.
        #         This helps handle edge cases like removing the first node.
        # Step 2: Initialize fast and slow pointers at the dummy node.
        # Step 3: Move the fast pointer n+1 steps forward to maintain a gap of n nodes.
        # Step 4: Move both fast and slow together until fast reaches the end.
        # Step 5: Now slow is right before the node to remove.
        # Step 6: Skip the target node using:
        #         slow.next = slow.next.next
        # Step 7: Return dummy.next (new head of list).
        dummy = ListNode(0)
        dummy.next = head
        
        fast = dummy
        slow = dummy

        # Move fast pointer n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next

        # Move both pointers
        while fast:
            fast = fast.next
            slow = slow.next

        # Remove the node
        slow.next = slow.next.next

        return dummy.next