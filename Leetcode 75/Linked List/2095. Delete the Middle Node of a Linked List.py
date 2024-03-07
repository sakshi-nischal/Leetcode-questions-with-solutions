# Approach 1: Using two pointer
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head):
        if not head.next:
            return None
        slow = head
        fast = head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next
        return head

"""
Time Complexity O(n)
Space Complexity O(1)
"""


# Approach 2: Using length of linked list
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head.next:
            return None
        length = 0
        current = head
        while current is not None:
            length += 1
            current = current.next
        
        count = 0
        length = length // 2
        counter = head

        while counter is not None:
            count += 1
            if count == (length):
                counter.next = counter.next.next
                break
            counter = counter.next

        return head

"""
Time Complexity O(n)
Space Complexity O(1)
"""

            
        
