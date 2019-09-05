# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#DON'T MAKE TAIL = ListNode(0) when there is already L1, L2 I can directly use.

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = temp = ListNode(0)

        #if both are present
        while l1 and l2:
            if (l1.val < l2.val):
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            
            # linking process of "new" at tail
            temp = temp.next
        
        temp.next = l1 if l1 else l2
            
        return head.next