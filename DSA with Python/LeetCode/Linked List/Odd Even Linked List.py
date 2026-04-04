# PROBLEM NUMBER: 328
# https://leetcode.com/problems/odd-even-linked-list/
# 328. Odd Even Linked List
# DIFFICULTY: MEDIUM

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Approach:
        # We need to rearrange the linked list such that:
        # • All nodes at odd indices come first
        # • Followed by all nodes at even indices
        #
        # Step 1: Handle edge cases:
        #         • If list is empty or has only one node → return head
        #
        # Step 2: Initialize pointers:
        #         • odd → points to first node (odd index)
        #         • even → points to second node (even index)
        #         • even_head → stores head of even list (to connect later)
        #
        # Step 3: Traverse the list while even and even.next exist:
        #         • Link current odd node to next odd node
        #           → odd.next = even.next
        #         • Move odd pointer forward
        #
        #         • Link current even node to next even node
        #           → even.next = odd.next
        #         • Move even pointer forward
        #
        # Step 4: After traversal:
        #         • Odd list is separated
        #         • Even list is separated
        #
        # Step 5: Connect end of odd list to head of even list
        #
        # Step 6: Return head

        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        # connect odd list with even list
        odd.next = even_head

        return head