# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        num2 = []
        
        while l1 is not None:
            num1.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            num2.append(l2.val)
            l2 = l2.next
        n1 = 0
        for i in range(len(num1)):
            n1 = n1 * 10 + num1[len(num1) -1 -i]
        
        n2 = 0
        for i in range(len(num2)):            
            n2 = n2 * 10 + num2[len(num2) -1 -i]
        print(num1, num2)
        sum_v = n1 + n2
        head = None
        if sum_v == 0:
            return ListNode(0)
        while sum_v:
            div = sum_v % 10
            sum_v //= 10
            
            if head is None:
                head = ListNode()
                head.val = div
                save_head = head
            else:
                tmp = ListNode(div)
                head.next = tmp
                head = tmp
        
        return save_head