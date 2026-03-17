# PROBLEM NUMBER: 83
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# 83. Remove Duplicates from Sorted List
# DIFFICULTY: EASY


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Approach:
        # We are given a sorted linked list and need to remove duplicate nodes
        # such that each element appears only once.
        
        # Step 1: Initialize a pointer "curr" pointing to the head of the linked list.
        
        # Step 2: Traverse the linked list while curr and curr.next exist.
        
        # Step 3: If the current node value is the same as the next node value,
        #         it means we found a duplicate.
        
        # Step 4: Remove the duplicate by skipping the next node:
        #         curr.next = curr.next.next
        
        # Step 5: If the values are different, move the curr pointer forward.
        
        # Step 6: Continue this process until we reach the end of the list.
        
        # Step 7: Return the head of the modified linked list.
        curr = head

        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head