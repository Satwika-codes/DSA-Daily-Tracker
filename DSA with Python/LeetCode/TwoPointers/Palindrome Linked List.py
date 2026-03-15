# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        # Approach:
        # We check whether a singly linked list is a palindrome.
        
        # Idea:
        # 1) Find the middle of the linked list using slow and fast pointers.
        # 2) Reverse the second half of the list.
        # 3) Compare the first half and the reversed second half.
        # 4) If all corresponding nodes match → it is a palindrome.


        if not head or not head.next:
            return True

        slow = fast = head

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

        # Compare both halves
        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True