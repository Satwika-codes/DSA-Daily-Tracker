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
        # ---------
        # We use the Two Pointers technique to calculate trapped rainwater efficiently.
        # 1. Initialize two pointers:
        # - left at the start of the array
        # - right at the end of the array
        # 2. Maintain two variables:
        # - left_max to store the maximum height seen from the left
        # - right_max to store the maximum height seen from the right
        # 3. Move the pointer with the smaller height:
        # - If height[left] < height[right], process the left side
        # - Otherwise, process the right side
        # 4. If the current height is less than the corresponding maximum,
        # water can be trapped and added to the total.
        # 5. Continue until the left and right pointers meet.
        # This approach runs in O(n) time and uses O(1) extra space.
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head:
            # If current value is duplicated
            if head.next and head.val == head.next.val:
                # Skip all nodes with this value
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
            else:
                prev = prev.next

            head = head.next

        return dummy.next
