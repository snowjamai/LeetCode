# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        DQ = deque()
        next_h = 1
        while next_h is not None:
            cur = head.val
            DQ.append(cur)
            next_h = head.next
            head = next_h
            
        while(len(DQ) > 1):
            p_l = DQ.popleft()
            p_r = DQ.pop()
            
            if p_l != p_r :
                return False
            
        return True
        