# PROBLEM NUMBER: 2039
# https://leetcode.com/problems/remove-linked-list-elements/
# 2039. Remove Linked List Elements
# DIFFICULTY:MEDIUM

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        remove_set = set(nums)

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        while curr:
            if curr.val in remove_set:
                prev.next = curr.next   # delete
            else:
                prev = curr             # move prev only if not deleted

            curr = curr.next

        return dummy.next