# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        Q = PriorityQueue()
        
        for i in lists:
            node = i
            
            while node is not None:
                Q.put(node.val)
                node = node.next
        answer_head = None        
        while not Q.empty():
            new_node = ListNode(Q.get())
            if answer_head is None:
                answer_head = new_node
                answer = answer_head
            else:
                answer.next = new_node
                answer = new_node
            
        return answer_head
        
        
        
        