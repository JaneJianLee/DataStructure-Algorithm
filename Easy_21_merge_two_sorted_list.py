# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# newhead      1 -> 3 -> 5 -> None
#              2 -> 4 -> 6 -> None


#Solution 1) Iterative Method

class IterativeSolution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        #newhead will be the return point of this function
        newhead = ListNode
        prev = newhead
        
        while l1 and l2:
            
            if l1.val < l2.val:
                
                prev.next = l1
                l1 = l1.next
                
            else:
                
                prev.next = l2
                l2=l2.next

            prev=prev.next
        
        prev.next = l1 if l1 is not None else l2
        
        return newhead.next


#Solution 2) Recursive Method

    class RecursiveSolution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        #base/escape case
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        
        #recursive part
        
        elif l1.val < l2.val:
            l1.next= self.mergeTwoLists(l1.next,l2)
            return l1

        else:
            l2.next= self.mergeTwoLists(l1,l2.next)
            return l2
    
                
