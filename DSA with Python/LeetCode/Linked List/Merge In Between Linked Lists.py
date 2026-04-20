# PROBLEM NUMBER: 1669
# https://leetcode.com/problems/merge-in-between-linked-lists/
# 1669. Merge In Between Linked Lists
# DIFFICULTY: MEDIUM

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        # Approach:
        # We need to remove nodes from index a to b in list1
        # and insert list2 in that position.
        #
        # Step 1: Find node just before index a (prevA)
        #
        # Step 2: Find node just after index b (afterB)
        #
        # Step 3: Connect prevA → list2
        #
        # Step 4: Traverse list2 to find its tail
        #
        # Step 5: Connect tail of list2 → afterB
        #
        # Step 6: Return list1 (modified in-place)

        # Step 1: find prevA
        prevA = list1
        for _ in range(a - 1):
            prevA = prevA.next

        # Step 2: find afterB
        afterB = prevA
        for _ in range(b - a + 2):
            afterB = afterB.next

        # Step 3: connect prevA → list2
        prevA.next = list2

        # Step 4: find tail of list2
        tail = list2
        while tail.next:
            tail = tail.next

        # Step 5: connect tail → afterB
        tail.next = afterB

        return list1