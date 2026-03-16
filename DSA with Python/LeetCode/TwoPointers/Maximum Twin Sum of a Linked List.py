# PROBLEM NUMBER: 257
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
# 257.Maximum Twin Sum of a Linked List
# DIFFICULTY: MEDIUM


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        # Approach:
        # We need to find the maximum twin sum in a linked list.
        # In a linked list of even length, the twin of node i is node (n-1-i).
        
        # Step 1: Use two pointers (slow and fast) to find the middle of the linked list.
        #         • slow moves one step at a time
        #         • fast moves two steps at a time
        #         When fast reaches the end, slow will be at the middle.
        
        # Step 2: Reverse the second half of the linked list starting from slow.
        
        # Step 3: Now we have:
        #         • first pointer starting from the head (first half)
        #         • second pointer starting from the reversed second half
        
        # Step 4: Traverse both halves simultaneously.
        #         For each pair of nodes, compute:
        #         twin_sum = first.val + second.val
        
        # Step 5: Track the maximum twin sum encountered.
        
        # Step 6: Move both pointers forward until the second half ends.
        
        # Step 7: Return the maximum twin sum.
        slow = head
        fast = head

        # Find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        # Calculate twin sums
        max_sum = 0
        first = head
        second = prev

        while second:
            max_sum = max(max_sum, first.val + second.val)
            first = first.next
            second = second.next

        return max_sum