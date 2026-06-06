# PROBLEM NUMBER: 445
# https://leetcode.com/problems/add-two-numbers-ii/
# 445. Add Two Numbers II
# DIFFICULTY: MEDIUM

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # Approach:
        # Since the digits are stored in
        # forward order, we cannot add them
        # directly from the head.
        #
        # First, store all digits of both
        # linked lists in two stacks.
        #
        # Then repeatedly pop digits from
        # the stacks, add them along with
        # the carry, and create nodes from
        # right to left.
        #
        # Each new node is inserted at the
        # front of the answer list, giving
        # the final result in correct order.

        s1 = []
        s2 = []

        while l1:
            s1.append(l1.val)
            l1 = l1.next

        while l2:
            s2.append(l2.val)
            l2 = l2.next

        carry = 0
        head = None

        while s1 or s2 or carry:

            x = s1.pop() if s1 else 0
            y = s2.pop() if s2 else 0

            total = x + y + carry

            carry = total // 10

            node = ListNode(total % 10)
            node.next = head
            head = node

        return head