# PROBLEM NUMBER: 21
# https://leetcode.com/problems/merge-two-sorted-lists/
# 21. Merge Two Sorted Lists
# DIFFICULTY: EASY


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Approach:
        # We need to merge two sorted linked lists into one sorted list.
        #
        # Step 1: Base cases:
        #         • If list1 is empty → return list2
        #         • If list2 is empty → return list1
        #
        # Step 2: Compare current nodes of both lists:
        #         • If list1.val < list2.val:
        #             → Choose list1 node
        #             → Recursively merge remaining list1 and list2
        #
        # Step 3: Otherwise:
        #         • Choose list2 node
        #         • Recursively merge list1 and remaining list2
        #
        # Step 4: Link chosen node to result of recursive call
        #
        # Step 5: Return the merged list head
        #
        # Step 6: Recursion continues until one list becomes empty

        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2