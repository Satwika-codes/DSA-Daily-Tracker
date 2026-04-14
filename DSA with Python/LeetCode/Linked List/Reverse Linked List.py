# PROBLEM NUMBER: 206
# https://leetcode.com/problems/reverse-linked-list/
# 206. Reverse Linked List
# DIFFICULTY: EASY

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Approach:
        # We need to reverse the linked list.
        #
        # Step 1: Initialize two pointers:
        #         • prev = None (will become new head)
        #         • curr = head (start of list)
        #
        # Step 2: Traverse the list:
        #         • For each node:
        #           → Store next node (to not lose reference)
        #
        # Step 3: Reverse the link:
        #         • curr.next = prev
        #
        # Step 4: Move pointers forward:
        #         • prev = curr
        #         • curr = next_node
        #
        # Step 5: Repeat until curr becomes None
        #
        # Step 6: prev will be new head of reversed list
        #
        # Step 7: Return prev

        prev = None
        curr = head

        while curr:
            next_node = curr.next   # store next
            curr.next = prev        # reverse link
            prev = curr             # move prev
            curr = next_node        # move curr

        return prev