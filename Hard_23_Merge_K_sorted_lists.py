# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        k=len(lists)
        if k==0:
            return None
        
        while k>1:
            counter = 0
            for i in range(0,k,2):
                if i+1 == k:
                    lists[counter]=lists[i]
                else:
                    lists[counter] = self.merge2lists(lists[i],lists[i+1]) 
                counter+=1
            
            #pop the elements that are not in use
            point = self.ceiling_div(k)
            del lists[point:]
            k = len(lists)
        
        return lists[0]

    def ceiling_div(self,num):
        carry,val=divmod(num,2)
        return carry+bool(val)
    
    def merge2lists(self, l1: ListNode, l2: ListNode) -> ListNode:
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

    