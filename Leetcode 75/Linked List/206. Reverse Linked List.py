# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

"""
- Here the algorithm works by first storing the next values in a temp variable called nxt and then assigning the values of curr.next = prev ( initailly None ).
- It then changes the prev value to the current value and finally current value to the next value stored in the nxt variable.
- We finally return the head of the reversed linkedList that is the prev.
Time COmplexity O(n)
Space COmplexity O(1)
"""

# Reference:
# https://youtu.be/G0_I-ZF0S38
