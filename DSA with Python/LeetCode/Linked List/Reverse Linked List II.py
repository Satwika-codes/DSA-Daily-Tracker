# PROBLEM NUMBER:92
# https://leetcode.com/problems/reverse-linked-list-ii/
# 92. Reverse Linked List II
# DIFFICLTY:MEDIUM

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        # Approach:
        # We need to reverse a part of the linked list
        # from position left to right (1-based index).
        #
        # Step 1: Handle edge case:
        #         • If list is empty or left == right → no change
        #
        # Step 2: Use dummy node:
        #         • Helps in handling edge cases (like reversing from head)
        #
        # Step 3: Move prev to node just before left position:
        #         • prev will point to (left - 1)th node
        #
        # Step 4: Start reversal:
        #         • curr points to left node
        #
        # Step 5: Reverse nodes between left and right:
        #         • Extract next node (temp)
        #         • Move temp to front of sublist
        #         • Adjust pointers accordingly
        #
        # Step 6: Repeat reversal process (right - left) times
        #
        # Step 7: Return dummy.next (new head)

        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Step 3: move prev to (left-1)
        for _ in range(left - 1):
            prev = prev.next

        # Step 4: reverse sublist
        curr = prev.next
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next