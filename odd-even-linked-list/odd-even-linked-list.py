# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even_head = None
        odd_head = None
        even = None
        odd =None
        cnt = 0
        
        if head is None:
            return None
     
        
        while head is not None:
            cnt += 1
            if cnt % 2 == 0:
                if even is None:
                    even = ListNode(head.val)
                    even_head = even
                else:
                    tmp = ListNode(head.val)
                    even.next = tmp
                    even = tmp
                    
            else:
                if odd is None:
                    odd = ListNode(head.val)
                    odd_head = odd
                else:
                    tmp = ListNode(head.val)                    
                    odd.next = tmp
                    odd = tmp
                    
            
            head = head.next
        
        
        odd.next = even_head

        return odd_head
                
    