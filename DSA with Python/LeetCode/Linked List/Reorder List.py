# PROBLEM NUMBER: 143
# https://leetcode.com/problems/reorder-list/
# 143. Reorder List
# DIFFICULTY: MEDIUM

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # Approach:
        # We need to reorder the list as:
        # L0 → Ln → L1 → Ln-1 → L2 → Ln-2 ...
        #
        # Step 1: Find the middle of the linked list:
        #         • Use slow and fast pointers
        #         • slow will reach the middle
        #
        # Step 2: Split and reverse second half:
        #         • Break the list into two halves
        #         • Reverse the second half of the list
        #
        # Step 3: Merge two halves:
        #         • Take one node from first half
        #         • Then one node from reversed second half
        #         • Repeat alternately
        #
        # Step 4: Continue until second half is exhausted
        #
        # Step 5: In-place modification, no extra space used

        if not head or not head.next:
            return

        # Step 1: find middle
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: reverse second half
        prev = None
        curr = slow.next
        slow.next = None  # split list

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # Step 3: merge two halves
        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2