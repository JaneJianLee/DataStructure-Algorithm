# Using Recursion in linked list : base case, test case... think about how the recursion ends and what needs to return for final solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        #base/escape case
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        
        #recursive part
        
        elif l1.val > l2.val:
            l1.next= self.mergeTwoLists(l1.next,l2)
            return l1

        else:
            l2.next= self.mergeTwoLists(l1,l2.next)
            return l2
    
        