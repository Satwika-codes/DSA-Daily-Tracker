# PROBLEM NUMBER: 61
# https://leetcode.com/problems/rotate-list/
# 61. Rotate List
# DIFFICULTY: MEDIUM

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # Approach:
        # We need to rotate the linked list to the right by k places.
        #
        # Step 1: Handle edge cases:
        #         • If list is empty, has one node, or k == 0 → return head
        #
        # Step 2: Find length of list and last node (tail)
        #
        # Step 3: Make the list circular:
        #         • Connect tail.next to head
        #
        # Step 4: Normalize k:
        #         • k = k % n (rotating n times gives same list)
        #
        # Step 5: Find new tail:
        #         • New tail is (n - k - 1)th node
        #
        # Step 6: New head:
        #         • Node after new tail
        #
        # Step 7: Break the circular link:
        #         • Set new_tail.next = None
        #
        # Step 8: Return new head

        if not head or not head.next or k == 0:
            return head

        # Step 2: find length and tail
        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1

        # Step 3: make circular
        tail.next = head

        # Step 4: normalize k
        k = k % n
        steps = n - k

        # Step 5: find new tail
        new_tail = head
        for _ in range(steps - 1):
            new_tail = new_tail.next

        # Step 6: new head
        new_head = new_tail.next

        # Step 7: break cycle
        new_tail.next = None

        return new_head